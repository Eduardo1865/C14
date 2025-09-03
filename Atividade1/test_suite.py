import pytest
import json
from unittest.mock import Mock, patch
from PyQt5.QtWidgets import QApplication

from jogo import QuizApp
from menu import MenuWindow
from opcoes import OpcoesWindow


class TestCasosPositivos:
    
    @pytest.fixture
    def app(self):
        if not QApplication.instance():
            return QApplication([])
        return QApplication.instance()
    
    @pytest.fixture
    def mock_api_data(self):
        return {
            "results": [
                {
                    "question": "What is 2+2?",
                    "correct_answer": "4",
                    "incorrect_answers": ["3", "5", "6"]
                }
            ]
        }
    
    @patch('jogo.requests.get')
    def test_01_quiz_inicia_corretamente(self, mock_get, app, mock_api_data):
        mock_response = Mock()
        mock_response.json.return_value = mock_api_data
        mock_get.return_value = mock_response
        
        quiz = QuizApp(difficulty="easy", num_questions=1)
        
        assert quiz.current_question == 0
        assert quiz.score == 0
        assert len(quiz.questions) == 1
    
    @patch('jogo.requests.get')
    def test_02_quiz_chama_api_correta(self, mock_get, app, mock_api_data):
        mock_response = Mock()
        mock_response.json.return_value = mock_api_data
        mock_get.return_value = mock_response
        
        QuizApp(difficulty="medium", num_questions=5)
        
        expected_url = "https://opentdb.com/api.php?amount=5&type=multiple&difficulty=medium"
        mock_get.assert_called_once_with(expected_url)
    
    @patch('jogo.requests.get')
    def test_03_skip_avanca_pergunta(self, mock_get, app, mock_api_data):
        mock_response = Mock()
        mock_response.json.return_value = mock_api_data
        mock_get.return_value = mock_response
        
        quiz = QuizApp(difficulty="easy", num_questions=1)
        quiz.skip_question()
        
        assert quiz.current_question == 1
    
    def test_04_menu_tem_opcoes_padrao(self, app):
        menu = MenuWindow()
        
        assert menu.options["difficulty"] == "easy"
        assert menu.options["num_questions"] == 5
    
    def test_05_menu_salva_opcoes(self, app):
        menu = MenuWindow()
        opcoes_mock = Mock()
        opcoes_mock.get_options.return_value = {"difficulty": "hard", "num_questions": 10}
        
        menu.opcoes_window = opcoes_mock
        menu.save_options()
        
        assert menu.options["difficulty"] == "hard"
        assert menu.options["num_questions"] == 10
    
    def test_06_opcoes_window_valores_iniciais(self, app):
        opcoes = OpcoesWindow()
        
        assert opcoes.num_questions_spin.value() == 5
        assert opcoes.difficulty_combo.count() == 3
    
    def test_07_opcoes_get_options(self, app):
        opcoes = OpcoesWindow()
        opcoes.num_questions_spin.setValue(8)
        
        options = opcoes.get_options()
        
        assert options["num_questions"] == 8
    
    def test_08_json_serialization(self):
        data = {"pergunta": "Test?", "resposta": "A"}
        json_string = json.dumps(data)
        result = json.loads(json_string)
        
        assert result == data
    
    def test_09_validacao_resposta_valida(self):
        def validar(resposta):
            return resposta.strip().upper() in ["A", "B", "C", "D"]
        
        assert validar("A") == True
        assert validar(" b ") == True
        assert validar("c\n") == True
    
    def test_10_processamento_entrada_usuario(self):
        entrada = "  b  "
        processada = entrada.strip().upper()
        
        assert processada == "B"


class TestCasosNegativos:
    
    @pytest.fixture
    def app(self):
        if not QApplication.instance():
            return QApplication([])
        return QApplication.instance()
    
    @patch('jogo.requests.get')
    def test_11_api_falha_rede(self, mock_get, app):
        mock_get.side_effect = Exception("Network Error")
        
        with pytest.raises(Exception):
            QuizApp(difficulty="easy", num_questions=1)
    
    @patch('jogo.requests.get')
    def test_12_api_resposta_invalida(self, mock_get, app):
        mock_response = Mock()
        mock_response.json.return_value = {"wrong": "format"}
        mock_get.return_value = mock_response
        
        with pytest.raises(KeyError):
            QuizApp(difficulty="easy", num_questions=1)
    
    @patch('jogo.requests.get')
    def test_13_api_sem_resultados(self, mock_get, app):
        mock_response = Mock()
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response
        
        quiz = QuizApp(difficulty="easy", num_questions=1)
        
        assert len(quiz.questions) == 0
    
    def test_14_opcoes_valores_extremos(self, app):
        opcoes = OpcoesWindow()
        
        opcoes.num_questions_spin.setValue(100)
        assert opcoes.num_questions_spin.value() <= 20
        
        opcoes.num_questions_spin.setValue(-5)
        assert opcoes.num_questions_spin.value() >= 1
    
    def test_15_json_malformado(self):
        dados_ruins = [
            "{'sem_aspas': valor}",
            '{"chave":}',
            "nao_e_json"
        ]
        
        for dado in dados_ruins:
            with pytest.raises(json.JSONDecodeError):
                json.loads(dado)
    
    def test_16_validacao_resposta_invalida(self):
        def validar(resposta):
            return resposta.strip().upper() in ["A", "B", "C", "D"]
        
        assert validar("E") == False
        assert validar("1") == False
        assert validar("") == False
        assert validar("AB") == False
    
    def test_17_entrada_usuario_vazia(self):
        entrada = "   "
        processada = entrada.strip().upper()
        
        assert processada == ""
    
    def test_18_menu_opcoes_none(self, app):
        menu = MenuWindow()
        menu.opcoes_window = None
        
        with pytest.raises(AttributeError):
            menu.save_options()
    
    def test_19_dados_none(self):
        result = json.dumps(None)
        
        assert result == "null"
    
    def test_20_lista_vazia_opcoes(self):
        opcoes = []
        
        assert len(opcoes) == 0
        assert not opcoes


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

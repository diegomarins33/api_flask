from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Diego',
        'habilidades': ['Python', 'Flask']},
    {
        'id': '1',
        'nome': 'Joãozinho',
        'habilidades': ['Java', 'Spring']}
    ]


# devolve um desenvolvedor pelo id, também altera e deleta:


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o ADM da API.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        try:
            desenvolvedores.pop(id)
            return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído.'})
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)


# lista todos os desenvolvedores e inclui um novo desenvolvedor:


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvoledores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)

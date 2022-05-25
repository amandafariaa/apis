from flask import Blueprint, make_response, jsonify, request

from app.models.estacoes import Estacoes
from app.models.estacoes_schemas import EstacoesSchema


class EstacoesController:

    estacoes_controller = Blueprint(name='estacoes_controller', import_name=__name__)

    @estacoes_controller.route('/estacoes', methods=['GET'])
    def index():
        lista_de_estacoes = Estacoes.query.all()
        estacoes_schema = EstacoesSchema(many=True)
        estacoes = estacoes_schema.dump(lista_de_estacoes)

        return make_response(jsonify({
            "estacoes": estacoes
        }))

    @estacoes_controller.route('/estacoes/<id>', methods=['GET'])
    def get_estacoes(id):
        estacoes = Estacoes.query.get(id)
        estacoes_schema = EstacoesController()
        estacoes = estacoes_schema.dump(estacoes)

        return make_response(jsonify({
            "estacoes": estacoes
        }))

    @estacoes_controller.route('/route', methods=['POST'])
    def create():
        dados = request.get_json()

        estacoes_schema = EstacoesSchema()
        estacoes = estacoes_schema.load(dados)
        estacoes = estacoes_schema.dump(estacoes.create())

        return make_response(jsonify({
            "estacoes": estacoes
        }), 201)

    @estacoes_controller.route('/estacoes/<id>', methods=['DELETE'])
    def delete(id):
        estacoes = estacoes.query.get(id)
        db.session.delete(estacoes)
        db.session.commit()
        return make_response(jsonify({}), 204)

    @estacoes_controller.route('/estacoes/<id>', methods=['PUT'])
    def put(id):
        estacoes = Estacoes.query.get(id)
        dados = request.get_json().get('estacoes')
        estacoes_schema = EstacoesSchema()

        if dados.get('id_estacao'):
            estacoes.id_estacao = dados['id_estacao']

        if dados.get('nome_estacao'):
            estacoes.nome_estacao = dados['nome_estacao']

        if dados.get('cod_regiao'):
            estacoes.cod_regiao = dados['cod_regiao']

        if dados.get('uf'):
            estacoes.uf = dados['uf']

        if dados.get('codigo_wmo'):
            estacoes.codigo_wmo = dados['codigo_wmo']

        if dados.get('latitude'):
            estacoes.latitude = dados['latitude']

        if dados.get('longitude'):
            estacoes.longitude = dados['longitude']

        if dados.get('data_fundacao'):
            estacoes.data_fundacao = dados['data_fundacao']

        db.session.add(estacoes)
        db.session.commit()

        estacoes_atualizado = estacoes_schema.dump(estacoes)

        return make_response(jsonify({"estacoes": estacoes_atualizado}), 200)
from flask import Flask, request, jsonify
import Util.bd as bd

app = Flask(__name__)


@app.route("/alunos", methods=["GET"])
def listar_alunos():
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        return (
            jsonify(
                [
                    {
                        "aluno_id": aluno[0],
                        "nome": aluno[1],
                        "endereco": aluno[2],
                        "cidade": aluno[3],
                        "estado": aluno[4],
                        "cep": aluno[5],
                        "pais": aluno[6],
                        "telefone": aluno[7],
                    }
                    for aluno in alunos
                ]
            ),
            200,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():
    data = request.get_json()
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                data["aluno_id"],
                data["nome"],
                data.get("endereco"),
                data.get("cidade"),
                data.get("estado"),
                data.get("cep"),
                data.get("pais"),
                data.get("telefone"),
            ),
        )
        conn.commit()
        return jsonify({"message": "Aluno cadastrado com sucesso"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route("/alunos/<string:aluno_id>", methods=["PUT"])
def alterar_aluno(aluno_id):
    data = request.get_json()
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE alunos
            SET nome = %s, endereco = %s, cidade = %s, estado = %s, cep = %s, pais = %s, telefone = %s
            WHERE aluno_id = %s
            """,
            (
                data["nome"],
                data.get("endereco"),
                data.get("cidade"),
                data.get("estado"),
                data.get("cep"),
                data.get("pais"),
                data.get("telefone"),
                aluno_id,
            ),
        )
        conn.commit()
        return jsonify({"message": "Dados do aluno atualizados com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route("/alunos/<string:aluno_id>", methods=["DELETE"])
def excluir_aluno(aluno_id):
    conn = bd.create_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM alunos WHERE aluno_id = %s", (aluno_id,))
        conn.commit()
        return jsonify({"message": "Aluno excluído com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

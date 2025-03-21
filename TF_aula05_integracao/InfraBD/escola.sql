CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    aluno_id VARCHAR(5) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    endereco VARCHAR(60),
    cidade VARCHAR(15),
    estado VARCHAR(15),
    cep VARCHAR(10),
    pais VARCHAR(15),
    telefone VARCHAR(24),
    PRIMARY KEY (aluno_id)
);

INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua das Flores, 123', 'São Paulo', 'SP', '01001-000', 'Brasil', '(11) 98765-4321'),
('A002', 'Maria Oliveira', 'Av. Paulista, 456', 'São Paulo', 'SP', '01310-000', 'Brasil', '(11) 91234-5678'),
('A003', 'Carlos Souza', 'Rua Afonso Pena, 789', 'Rio de Janeiro', 'RJ', '20040-001', 'Brasil', '(21) 99876-5432'),
('A004', 'Ana Costa', 'Av. Atlântica, 321', 'Rio de Janeiro', 'RJ', '22070-000', 'Brasil', '(21) 98765-1234'),
('A005', 'Pedro Santos', 'Rua XV de Novembro, 654', 'Curitiba', 'PR', '80020-310', 'Brasil', '(41) 91234-8765'),
('A006', 'Fernanda Lima', 'Av. Sete de Setembro, 987', 'Salvador', 'BA', '40060-001', 'Brasil', '(71) 99876-4321'),
('A007', 'Lucas Almeida', 'Rua das Palmeiras, 111', 'Belo Horizonte', 'MG', '30140-120', 'Brasil', '(31) 98765-6789'),
('A008', 'Juliana Pereira', 'Av. Brasil, 222', 'Porto Alegre', 'RS', '90010-000', 'Brasil', '(51) 91234-5678'),
('A009', 'Rafael Mendes', 'Rua Amazonas, 333', 'Manaus', 'AM', '69010-060', 'Brasil', '(92) 99876-5432'),
('A010', 'Camila Rocha', 'Av. Rio Branco, 444', 'Recife', 'PE', '50030-310', 'Brasil', '(81) 98765-1234');
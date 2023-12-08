CREATE DATABASE n3;
USE n3;
create table if not exists USUARIOS(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
email varchar(255) not null,
nome varchar(255) not null,
sobrenome varchar(255) not null,
ativo tinyint default 1,
criado_em datetime,
alterado_em datetime);

DELIMITER //
CREATE TRIGGER trg_criacao_usuarios
BEFORE INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    END;
//
CREATE TRIGGER trg_atualizacao_usuarios
BEFORE UPDATE ON USUARIOS
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists CREDENCIAIS(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome varchar(255) not null,
criado_em datetime,
alterado_em datetime);

DELIMITER //
CREATE TRIGGER trg_criacao_credenciais
BEFORE INSERT ON CREDENCIAIS
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_credenciais
BEFORE UPDATE ON CREDENCIAIS
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists USUARIOS_CREDENCIAIS(
id_usuario INTEGER NOT NULL,
id_credencial integer not null,
criado_em datetime,
alterado_em datetime,
primary key(id_usuario, id_credencial),
foreign key (id_usuario) references usuarios(id),
foreign key (id_credencial) references credenciais(id));
    
DELIMITER //
CREATE TRIGGER trg_criacao_usuarios_credenciais
BEFORE INSERT ON USUARIOS_CREDENCIAIS
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_usuarios_credenciais
BEFORE UPDATE ON USUARIOS_CREDENCIAIS
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists CUPONS(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
codigo varchar(255) not null,
descricao varchar(10000),
ativo tinyint default 1,
valor numeric,
multiplo tinyint default 0,
data_inicio datetime,
data_fim datetime,
criado_em datetime,
alterado_em datetime);

DELIMITER //
CREATE TRIGGER trg_criacao_cupons
BEFORE INSERT ON CUPONS
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_cupons
BEFORE UPDATE ON CUPONS
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists SESSOES(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
data date,
criado_em datetime,
alterado_em datetime);

DELIMITER //
CREATE TRIGGER trg_criacao_sessoes
BEFORE INSERT ON SESSOES
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_sessoes
BEFORE UPDATE ON SESSOES
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists PEDIDOS(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
data_pedido date not null,
total numeric not null,
id_cupom integer,
id_sessao integer,
id_usuario integer,
criado_em datetime,
alterado_em datetime,
foreign key (id_cupom) references cupons(id),
foreign key (id_sessao) references sessoes(id),
foreign key (id_usuario) references usuarios(id));

DELIMITER //
CREATE TRIGGER trg_criacao_pedidos
BEFORE INSERT ON PEDIDOS
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_pedidos
BEFORE UPDATE ON PEDIDOS
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists TRANSACAO_CC(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
codigo varchar(255),
id_pedido integer not null,
data_transacao datetime,
operador varchar(255) not null,
valor numeric not null,
num_cc varchar(255),
resposta varchar(255),
criado_em datetime,
alterado_em datetime,
foreign key (id_pedido) references pedidos(id));

DELIMITER //
CREATE TRIGGER trg_criacao_transacao_cc
BEFORE INSERT ON TRANSACAO_CC
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_transacao_cc
BEFORE UPDATE ON TRANSACAO_CC
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table categorias(
    id integer not null auto_increment,
    nome varchar(255) not null,
    id_categoria_pai integer,
    criado_em datetime,
    alterado_em datetime,
    primary key(id),
    foreign key (id_categoria_pai) references categorias(id)
);

DELIMITER //
CREATE TRIGGER trg_criacao_categorias
BEFORE INSERT ON categorias
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_categorias
BEFORE UPDATE ON categorias
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table status_produtos(
    id integer not null auto_increment,
    nome varchar(255) not null,
    criado_em datetime,
    alterado_em datetime,
    primary key(id)
);

DELIMITER //
CREATE TRIGGER trg_criacao_produtos_status_produtos
BEFORE INSERT ON status_produtos
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_status_produtos
BEFORE UPDATE ON status_produtos
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table produtos(
    id integer not null auto_increment,
    cod_barras varchar(255) not null,
    descricao text,
    id_status_produto integer not null,
    preco_normal numeric,
    preco_com_desconto numeric,
    quantidade integer,
    criado_em datetime,
    alterado_em datetime,
    primary key(id),
    foreign key (id_status_produto) references status_produtos(id)
);

DELIMITER //

CREATE TRIGGER trg_criacao_produtos
BEFORE INSERT ON produtos
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_produtos
BEFORE UPDATE ON produtos
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table produtos_categorias(
    id_categoria integer,
    id_produto integer,
    criado_em datetime,
    alterado_em datetime,
    primary key(id_categoria,id_produto),
    foreign key (id_categoria) references categorias(id),
    foreign key (id_produto) references produtos(id)
);

DELIMITER //

CREATE TRIGGER trg_criacao_produtos_categorias
BEFORE INSERT ON produtos_categorias
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_produtos_categorias
BEFORE UPDATE ON produtos_categorias
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table tags(
id integer not null auto_increment,
nome varchar(255) not null,
criado_em datetime,
alterado_em datetime,
primary key(id)
);

DELIMITER //
CREATE TRIGGER trg_criacao_tags
BEFORE INSERT ON tags
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_tags
BEFORE UPDATE ON tags
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table produtos_tags(
    id_produto integer,
    id_tag integer,
    criado_em datetime,
    alterado_em datetime,
    primary key(id_produto,id_tag),
    foreign key (id_produto) references produtos(id),
    foreign key (id_tag) references tags(id)
);

DELIMITER //
CREATE TRIGGER trg_criacao_produtos_tags
BEFORE INSERT ON produtos_tags
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_produtos_tags
BEFORE UPDATE ON produtos_tags
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create table if not exists PRODUTOS_PEDIDOS(
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
id_pedido integer,
id_produto integer,
cod_barras varchar(255) not null,
nome varchar(255) not null,
descricao varchar(10000),
preco numeric not null,
quantidade integer not null,
subtotal numeric not null,
criado_em datetime,
alterado_em datetime,
foreign key (id_pedido) references pedidos(id),
foreign key (id_produto) references produtos(id));

DELIMITER //
CREATE TRIGGER trg_criacao_produtos_pedidos
BEFORE INSERT ON produtos_pedidos
FOR EACH ROW
BEGIN
    SET NEW.criado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
CREATE TRIGGER trg_atualizacao_produtos_pedidos
BEFORE UPDATE ON produtos_pedidos
FOR EACH ROW
BEGIN
    SET NEW.alterado_em = CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-03:00');
END;
//
DELIMITER ;

create view view_compras_do_usuario as
select usuarios.id as "ID_usuario", usuarios.nome as nome, pedidos.data_pedido as "Data do pedido", pedidos.total as "Total do pedido"
from usuarios
join pedidos 
on usuarios.id = pedidos.id_usuario;

create view view_produtos_com_tag as
SELECT tags.id as "IDtag", produtos.cod_barras as 'Código de barras', produtos.descricao AS 'Produto', tags.nome AS 'Tag', produtos.preco_normal AS 'Preco' 
FROM produtos 
LEFT JOIN produtos_tags
ON produtos.id = produtos_tags.id_produto
LEFT JOIN tags 
ON produtos_tags.id_tag = tags.id;

INSERT INTO USUARIOS (email, nome, sobrenome) VALUES
('alice@email.com', 'Alice', 'Silva'),
('bob@email.com', 'Bob', 'Santos'),
('carol@email.com', 'Carol', 'Oliveira'),
('david@email.com', 'David', 'Pereira'),
('elaine@email.com', 'Elaine', 'Souza'),
("montes@icloud.net","Erica Mueller","Beck"),
  ("velit@outlook.ca","Alice Blake","Oneal"),
  ("consectetuer.mauris.id@yahoo.org","Dawn Ferrell","Evans"),
  ("mollis.integer@hotmail.edu","Gisela Stevens","Warner"),
  ("eget@hotmail.net","Francis Lowery","Weaver"),
  ("enim.commodo@outlook.net","Vladimir English","Howell"),
  ("lectus@google.org","Lydia Thornton","Cooke"),
  ("euismod.ac.fermentum@aol.ca","Vincent Mcguire","Mcdonald"),
  ("in@outlook.edu","Channing Morton","Mccullough"),
  ("odio.a.purus@outlook.com","Josephine Lawson","Duncan"),
  ("morbi.neque.tellus@protonmail.couk","Abraham Holloway","Moody"),
  ("ipsum@icloud.edu","Clark Chan","Velez"),
  ("lacus.cras@hotmail.couk","Leo Craig","George"),
  ("fames.ac@icloud.com","Mufutau Marks","Trujillo"),
  ("interdum.sed@aol.net","Brielle Joyce","Michael"),
  ("semper.et@yahoo.com","Austin O'brien","Tyson"),
  ("nisi.sem@protonmail.couk","Blythe Thornton","Mckee"),
  ("a.tortor@aol.edu","Lana Duncan","Lane"),
  ("aliquam.ornare@protonmail.net","Giacomo Wynn","Romero"),
  ("libero.donec@outlook.edu","Fitzgerald Barber","Cameron"),
  ("tortor.at@icloud.com","Tiger Lindsay","King"),
  ("morbi@hotmail.edu","Vincent Bartlett","Smith"),
  ("et.euismod@icloud.com","Kieran Oliver","Holloway"),
  ("enim.sit@hotmail.couk","Shoshana Hunt","Kelly"),
  ("nunc@hotmail.com","Judith Wong","Dominguez"),
  ("non.dapibus@outlook.com","Bernard Holden","Love"),
  ("lacinia.at@hotmail.net","Medge Stephenson","Blanchard"),
  ("ipsum@hotmail.edu","Yuri Fernandez","Harris"),
  ("et@protonmail.edu","Felicia Parrish","Oneil"),
  ("eu.placerat@outlook.com","Wade Whitaker","Johnston"),
  ("et.commodo.at@aol.ca","Vivian Bishop","Meadows"),
  ("sem@icloud.com","Harrison Rasmussen","Christensen"),
  ("felis@outlook.org","Remedios Dalton","Mcneil"),
  ("libero@outlook.edu","TaShya Moran","Barber"),
  ("mauris.non@outlook.ca","Jin Floyd","Flowers"),
  ("feugiat.nec.diam@icloud.net","Marsden Salazar","Huber"),
  ("posuere.vulputate@icloud.ca","Debra Bush","Morris"),
  ("ut.cursus.luctus@icloud.couk","Vaughan Case","Lloyd"),
  ("lectus.rutrum.urna@protonmail.edu","Hector Mcfarland","Salazar"),
  ("nullam.scelerisque.neque@hotmail.ca","Tamekah Poole","Cooke"),
  ("duis.volutpat@yahoo.com","Isabella Mckinney","Talley"),
  ("nec.metus@hotmail.edu","Jael Blevins","Callahan"),
  ("facilisis.non@yahoo.org","Zenia Vance","Macias"),
  ("ultricies.dignissim.lacus@hotmail.couk","Noble Ferrell","Small"),
  ("cursus.purus@icloud.couk","Nathan Thompson","Turner"),
  ("blandit.enim.consequat@google.com","Lana Meyers","Sanford"),
  ("dictum.proin@google.net","Coby Leon","Rocha"),
  ("eget@protonmail.edu","Dara Stone","Palmer"),
  ("etiam@protonmail.edu","Brenna Smith","Richmond"),
  ("non.nisi.aenean@icloud.com","Garth Martin","Vincent");

INSERT INTO CREDENCIAIS (nome) VALUES
('credencial_padrao'),
('credencial_admin'),
('credencial_vip');

INSERT INTO USUARIOS_CREDENCIAIS (id_usuario, id_credencial) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(5, 1);

INSERT INTO CUPONS (codigo, descricao, valor, data_inicio, data_fim) VALUES
('DESC10', 'Desconto de 10%', 10.00, '2023-01-01', '2023-12-31'),
('FRETEGRATIS', 'Frete Grátis', NULL, '2023-02-01', '2023-06-30'),
('ANIVERSARIO', 'Cupom de Aniversário', 20.00, '2023-03-15', '2023-03-20');

INSERT INTO SESSOES (data) VALUES
('2023-01-05'),
('2023-02-10'),
('2023-03-20'),
('2023-04-15'),
('2023-05-25');

INSERT INTO PEDIDOS (data_pedido, total, id_cupom, id_sessao, id_usuario) VALUES
('2023-01-15', 120.00, 1, 1, 1),
('2023-02-20', 50.00, 2, 2, 2),
('2023-03-25', 200.00, 3, 3, 3),
('2023-04-30', 80.00, NULL, 4, 4),
('2023-05-05', 150.00, 1, 5, 5);

INSERT INTO TRANSACAO_CC (codigo, id_pedido, data_transacao, operador, valor, num_cc, resposta) VALUES
('TRANS101', 1, '2023-01-16 10:30:00', 'OperadorA', 120.00, '1111222233334444', 'Aprovada'),
('TRANS202', 2, '2023-02-21 11:45:00', 'OperadorB', 50.00, '5555666677778888', 'Aprovada'),
('TRANS303', 3, '2023-03-26 14:20:00', 'OperadorC', 200.00, '9999000011112222', 'Aprovada'),
('TRANS404', 4, '2023-05-01 09:00:00', 'OperadorD', 80.00, '1234123412341234', 'Aprovada'),
('TRANS505', 5, '2023-05-06 16:30:00', 'OperadorE', 150.00, '9876987698769876', 'Aprovada');

INSERT INTO categorias (nome) VALUES
('Eletrônicos'),
('Roupas'),
('Alimentos'),
('Livros');

INSERT INTO status_produtos (nome) VALUES
('Disponível'),
('Indisponível');

INSERT INTO produtos (cod_barras, descricao, id_status_produto, preco_normal, preco_com_desconto, quantidade) VALUES
('123456789', 'Smartphone Top', 1, 1200.00, 1000.00, 50),
('987654321', 'Camiseta Estilosa', 1, 50.00, NULL, 100),
('111222333', 'Arroz Integral', 1, 10.00, NULL, 200),
('444555666', 'Livro de Ficção', 1, 30.00, 25.00, 30),
('777888999', 'Fones de Ouvido', 2, 80.00, NULL, 80);

INSERT INTO produtos_categorias (id_categoria, id_produto) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(1, 5);

INSERT INTO tags (nome) VALUES
('Promoção'),
('Lançamento'),
('Orgânico'),
('Tecnologia');

INSERT INTO produtos_tags (id_produto, id_tag) VALUES
(1, 4),
(2, 1),
(3, 3),
(4, 2),
(5, 4);

INSERT INTO PRODUTOS_PEDIDOS (id_pedido, id_produto, cod_barras, nome, descricao, preco, quantidade, subtotal) VALUES
(1, 1, '123456789', 'Smartphone Top', 'Último modelo com câmera de alta resolução', 1000.00, 2, 2000.00),
(2, 2, '987654321', 'Camiseta Estilosa', 'Camiseta de algodão com estampa exclusiva', 50.00, 3, 150.00),
(3, 3, '111222333', 'Arroz Integral', 'Pacote de 1kg de arroz integral orgânico', 10.00, 5, 50.00),
(4, 4, '444555666', 'Livro de Ficção', 'Best-seller do ano, emocionante e envolvente', 25.00, 1, 25.00),
(5, 5, '777888999', 'Fones de Ouvido', 'Fones de ouvido sem fio com cancelamento de ruído', 80.00, 2, 160.00);
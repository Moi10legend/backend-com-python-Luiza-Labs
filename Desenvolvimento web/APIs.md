Desenvolvimento web se refere ao processo de criação de websites e aplicações para a internet (acessível publicamente através de um endereço) ou uma intranet (aplicações em contexto de redes privadas). Abrange uma variedade de tarefas incluindo web design, programação web, gestão de banco de dados e engenharia de servidores.

## Componentes principais:
Front-end: A parte do website que os usuários interagem diretamente. Envolve a criação de interfaces de usuário e experiências, usando tecnologias como HTML, CSS e Javascript. O objetivo é apresentar informações de forma interativa e acessível para o usuário final.
Back-end: Onde ocorrem os processamentos de dados, gerenciamento de banco de dados e controle de servidor. Envolve linguagens como Python, Java, Go, PHP, Ruby etc. Para o banco de dados: PostgreSQL, MySQL, MongoDB, Oracle. Também existem frameworks: Django(Python), Express(JavaScript) e Spring Boot (Java).

## Internet vs Web
A internet é uma rede global computadores interconectados. A Web ou World Wide Web, é um sistema de informações que utiliza o protocolo HTTP para transmitir dados.
O HTTP (Hypertext Transfer Protocol) é o protocolo fundamental usado na web para transferência de dados. Quando um usuário acessa um site, o navegador envia uma solicitação HTTP para o servidor do site, que responde com os dados do site.

## Funcionamento de um web site:
1º  Solicitação do usuário: Tudo começa com o usuário inserido um URL no navegador ou clicando em um link.
2º Resolução de DNS: O URL é traduzido em um endereço IP através de um sistema chamado DNS (Domain Name System).
3º Conexão com o servidor: O navegador utiliza o endereço IP para estabelecer uma conexão com o servidor que hospeda o site.
4º Resposta do servidor: O servidor processa a solicitação HTTP e envia de volta os arquivos, geralmente em HTML, CSS e JavaScript. 
5º Renderização no navegador: O navegador interpreta esses arquivos e exibe o site ao usuário.
Tecnologias envolvidas
Além do HTML, CSS e JavaScript, tecnologias como SSL/TLS para segurança, APIs para interatividade e Banco de Dados para armazenamento de dados.

## APIs e seus conceitos fundamentais
API ou interface de programação de aplicações, é um conjunto de regras e definições que permite que diferentes aplicações de software ou componentes se comuniquem entre si. Funciona como um intermediário, permitindo que pedidos sejam feitos e respostas sejam recebidas.
Na web, elas são utilizadas para permitir a interação entre diferentes serviços e aplicações, como enviar dados de um usuário de um aplicativo para um servidor ou solicitar dados de um serviço externo como redes sociais, maps e clima (previsão do tempo).
Tipos de API
API Restful: Se refere a APIs que seguem os princípios do Rest (Representational State Transfer). São baseadas em padrões HTTP e utilizadas para interações web. Algumas de suas características são:
•	Uso dos métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD.
•	Curva de aprendizado menor
•	Fácil de entender e implementar
API SOAP: Simple Object Access Protocol é um protocolo que define um padrão para troca de mensagens baseadas em XML. Características do SOAP:
•	Protocolo baseado em XML para troca de informações
•	Independente de linguagem e plataforma de transporte.
•	Suporte para aplicações complexas e segurança avançada.
API GraphQL: Uma linguagem de consulta para API, e um servidor capaz de executar essas consultas, retornando apenas os dados especificados. Características:
•	Permite que os clientes especifiquem exatamente quais dados querem.
•	Eficiente na redução de solicitações e no tamanho dos dados transferidos.
•	Flexível e fortemente tipada, facilitando a evolução da API.
A escolha do tipo de API vem da necessidade específica do projeto, recursos disponíveis e da expertise da equipe. Restful é popular pela simplicidade, SOAP é preferido para segurança e transações complexas, enquanto GraphQL é ideal para aplicações que requerem dados dinâmicos e personalizados.

## Verbos HTTP em APIs RestFul
GET é para leitura, POST para criação, PUT/PATCH para atualização e DELETE para remoção.
O PUT vai substituir completamente um recurso existente no servidor e o PATCH faz uma atualização parcial, atualizando apenas um campo ou alguns recursos.

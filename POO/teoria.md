# Encapsulamento

Em Python, não temos palavras reservadas para determinar o nível de acesso dos atributos e métodos da classe, mas usam-se convenções no nome do recurso, para definir se a variável é pública ou privada.
Coloca-se um underline antes do nome do método/atributo para indicar que ele é privado.

# Properties

Com o property() você pode criar atributos computados/gerenciados em sua classe. Você os utiliza quando precisa modificar sua implementação interna sem alterar a API pública da classe

# Polimorfismo
Na programação, polimorfismo significa o mesmo nome da função (mas assinaturas diferentes) sendo usado para tipos diferentes. Então, é possível modificar um método herdado da classe pai na classe filha.

# Métodos de classe e estáticos

Os métodos de classe pertencem à classe e não à instância. Eles possuem acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe. Chamamos esse parâmetro de cls (por convenção)

Os métodos estáticos não recebem um primeiro argumento explícito. Ele também é um método da classe, porém, não pode acessar e nem modificar o acesso da classe.

Geralmente, os métodos de classe são utilizados para criar métodos de fábrica e os estáticos para criar funções utilitárias.

# Interface

Interfaces definem o que uma classe deve fazer, e não como. Ou seja, a definição de um contrato onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. No Python, são criadas classes abstratas, que não podem ser instanciadas. Elas são criadas através do módulo ABC, pois o Python não cria classes abstratas por ele próprio. O ABC funciona decorando métodos da classe base como abstratos. Um método se torna abstrato quando decorado com @abstractmethod.
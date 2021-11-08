# BLOG

> Objetivo desta aplicação é criar publicações para um blog

&nbsp;

## Registrar uma nova Publicação

---

### **Post** - /posts

##### Exemplo de Entrda:

```
{
	"title": "Deixada para trás",
	"author": "Charlie Donlea",
	"tags": ["suspense", "ficção"],
	"content": "Sem inimigos, nem suspeitos. Apenas uma pessoa"
}
```

##### Exemplo de Retorno:

```
{
  "author": "Charlie Donlea",
  "content": "Sem inimigos, nem suspeitos. Apenas uma pessoa",
  "created_at": "Mon, 08 Nov 2021 13:35:13 GMT",
  "id": 5,
  "tags": [
    "suspense",
    "ficção"
  ],
  "title": "Deixada para trás",
  "updated_at": "Mon, 08 Nov 2021 13:35:13 GMT"
}
```

&nbsp;

## Ler uma publicação específica

---

### **GET** - /posts/id

##### Exemplo de Retorno

```
{
  "author": "Charlie Donlea",
  "content": "Sem inimigos, nem suspeitos. Apenas uma pessoa",
  "created_at": "Mon, 08 Nov 2021 13:35:13 GMT",
  "id": 5,
  "tags": [
    "suspense",
    "ficção"
  ],
  "title": "Deixada para trás",
  "updated_at": "Mon, 08 Nov 2021 13:35:13 GMT"
}
```

&nbsp;

## Ler todas as publicações

---

### **GET** - /posts

##### Exemplo de Retorno

```
[
  {
    "author": "Charlie Donlea",
    "content": "Sem inimigos, nem suspeitos. Apenas uma pessoa",
    "created_at": "Mon, 08 Nov 2021 13:35:13 GMT",
    "id": 5,
    "tags": [
      "suspense",
      "ficção"
    ],
    "title": "Deixada para trás",
    "updated_at": "Mon, 08 Nov 2021 13:35:13 GMT"
  },
  {
    "author": "Charlie Donlea",
    "content": "Se aceitar o convite, não ignore o aviso",
    "created_at": "Mon, 08 Nov 2021 13:40:36 GMT",
    "id": 6,
    "tags": [
      "suspense",
      "ficção"
    ],
    "title": "Nunca saia sozinho",
    "updated_at": "Mon, 08 Nov 2021 13:40:36 GMT"
  }
]
```

&nbsp;

## Atualizar uma publicação

---

### **PATCH** - /posts/id

##### Exemplo de Entrada:

```
{
	"title": "O controle perfeito"
}
```

##### Exemplo de Retorno:

```
{
  "author": "Charlie Donlea",
  "content": "Sem inimigos, nem suspeitos. Apenas uma pessoa",
  "created_at": "Mon, 08 Nov 2021 13:35:13 GMT",
  "id": 5,
  "tags": [
    "suspense",
    "ficção"
  ],
  "title": "O controle perfeito",
  "updated_at": "Mon, 08 Nov 2021 13:35:13 GMT"
}
```

&nbsp;

## Deletar uma publicação

---

### **DELETE** - /posts/id

##### Exemplo de Retorno:

```
{
  "author": "Charlie Donlea",
  "content": "Se aceitar o convite, não ignore o aviso",
  "created_at": "Mon, 08 Nov 2021 13:40:36 GMT",
  "id": 6,
  "tags": [
    "suspense",
    "ficção"
  ],
  "title": "O controle perfeito",
  "updated_at": "Mon, 08 Nov 2021 13:44:11 GMT"
}
```

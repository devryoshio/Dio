# Desafio 

Cria para dectentar a pessoa famoso,  o [data set](https://github.com/digitalinnovationone/nexa-analise-avancada-de-imagens-e-texto-com-ia-na-aws/tree/main/reconhecimento_celebridades) 


O **Amazon Rekognition** é um serviço da AWS que permite analisar imagens e vídeos para identificar objetos, cenas, atividades e até **rostos de celebridades**. Vou te mostrar como configurar e usar o **Rekognition** para identificar celebridades em imagens.

---

### **1. Configuração Inicial**

#### a) **Criar uma Conta na AWS e Configurar o IAM**
1. Se ainda não tiver, crie uma conta no [AWS](https://aws.amazon.com/).
2. Vá para o [IAM (Identity and Access Management)](https://console.aws.amazon.com/iam/):
   - Crie um usuário com permissões para o serviço **Amazon Rekognition**.
   - **Permissões necessárias:** `AmazonRekognitionFullAccess`.

#### b) **Instalar o AWS CLI e Configurar Credenciais**
1. **Instalar o AWS CLI:**
   ```bash
   sudo apt-get install awscli  # Para Linux (Ubuntu)
   ```

2. **Configurar suas credenciais:**
   ```bash
   aws configure
   ```
   - **AWS Access Key ID:** (gerado no IAM)
   - **AWS Secret Access Key:** (chave secreta gerada)
   - **Region:** ex: `us-east-1`
   - **Output format:** `json`

---

### **2. Instalando o Boto3 (SDK da AWS para Python)**

O **Boto3** é a biblioteca Python para interagir com serviços da AWS.

```bash
pip install boto3
```

---

### **3. Código Python para Reconhecer Celebridades**

Aqui está um exemplo de como identificar rostos de celebridades em uma imagem usando o **Amazon Rekognition**.

#### **Reconhecimento de Celebridades com Imagem Local:**

```python
import boto3

# Inicializa o cliente Rekognition
rekognition = boto3.client('rekognition')

# Caminho da imagem local
image_path = 'caminho_para_sua_imagem.jpg'

# Lê a imagem
with open(image_path, 'rb') as image_file:
    image_bytes = image_file.read()

# Chama o serviço de reconhecimento de celebridades
response = rekognition.recognize_celebrities(Image={'Bytes': image_bytes})

# Exibe os resultados
for celebrity in response['CelebrityFaces']:
    print(f"Nome: {celebrity['Name']}")
    print(f"Confiança: {celebrity['MatchConfidence']:.2f}%")
    print(f"URLs: {celebrity['Urls']}")
    print('---')

# Verifica se há rostos não reconhecidos
if response['UnrecognizedFaces']:
    print(f"Rostos não reconhecidos: {len(response['UnrecognizedFaces'])}")
else:
    print("Todos os rostos foram reconhecidos!")
```

---

### **4. Usando Imagens no Amazon S3**

Se você preferir usar imagens armazenadas no **Amazon S3**, o código seria assim:

```python
response = rekognition.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'nome-do-seu-bucket',
            'Name': 'caminho/para/sua_imagem.jpg'
        }
    }
)

# Exibe os resultados
for celebrity in response['CelebrityFaces']:
    print(f"Nome: {celebrity['Name']}")
    print(f"Confiança: {celebrity['MatchConfidence']:.2f}%")
    print(f"URLs: {celebrity['Urls']}")
    print('---')
```

---

### **5. Resultados Esperados**

O retorno da função `recognize_celebrities` inclui:
- **Name**: Nome da celebridade reconhecida.
- **MatchConfidence**: Nível de confiança no reconhecimento (em %).
- **Urls**: URLs com informações sobre a celebridade (por exemplo, links da Wikipedia ou IMDb).
- **UnrecognizedFaces**: Caso algum rosto não seja identificado.

---

### **6. Solução de Problemas**

- **Permissão negada:** Verifique se o usuário tem a política `AmazonRekognitionFullAccess`.
- **Erro de formato:** O serviço aceita imagens nos formatos **JPEG** e **PNG**.
- **Região incompatível:** O **Rekognition** pode não estar disponível em todas as regiões. Tente configurar para `us-east-1` ou `us-west-2`.


# 30DaysOf Blog Scafolding

The #30DaysOf Python app will scaffold out the blog structure for a #30Days blog campaign.

1. The index.md file will be created for each day from the template.md file.
1. The blog.yaml file will be used to configure the metadata for each day.

## Installation

Tested on:

1. macOS (Venture)
1. Windows 11 on Intel and Windows 11 on ARM
1. Ubuntu 20.04/22.04 on Intel and ARM.

```bash
pip3 install -r requirements.txt
```

## Content Configuration

Use VS Code with the [RedHat YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) extension installed to validate the blog.yaml file against the blog.json schema.

A blog.yaml file is used to configure the structure and the metadata of the blog posts. You'll find the blog.yaml file in the root of the project.

### Example blog.yaml

```yaml
{
campaign:
  name: "30DaysOfAzureAI"
  static_img_folder: "./../../static/img/2023-aia"
  static_img_path: "https://azureaidevs.github.io/hub/img/2023-aia"
  daily_blog_url: "https://azureaidevs.github.io/hub/2023-aia"
  social_tags: "#30DaysOfAzureAI #AzureAiDevs #AI"


  days:
    - folder: "2023-03-29-kickoff"
      emoji: 🏁
      audience: "Azure AI Developers"
      title: "Kick Starting AI April!"
      description: "Welcome to #AiApril! Join us for #30DaysOfAzureAI learning, skilling and discussions at [AI April](https://aka.ms/ai-april)"
      authors: [Dave]
      keywords: [Azure-AI, Azure-OpenAI-Services, Cognitive-Services, Machine-Learning, Cognitive-Search, dotnet, onnx, CoPilot]
      tags: [azure-ai,azure-ml,azure-open-ai,azure-cognitive-services,responsible-ai,azure-ai-fundamentals,30-days-of-azure-ai]
      canonical:


    - folder: "2023-04-03-azure-openai-services"
      emoji: 🏁
      audience: "Azure AI Developers"
      title: "Unleash the power of Azure OpenAI"
      description: "Unleashing the power of AI with Azure OpenAI: A simple guide to get started"
      authors: [Meer]
      keywords: [Azure-OpenAI-Services, Machine-Learning, Azure-AI]
      tags: [azure-ai, azure-open-ai, 30-days-of-azure-ai]
      social_tag: "#OpenAI"
      canonical: https://techcommunity.microsoft.com/t5/fasttrack-for-azure/unleashing-the-power-of-ai-with-azure-openai-a-simple-guide-to/ba-p/3725706
      references:
      - "[Azure OpenAI Service](https://azure.microsoft.com/products/cognitive-services/openai-service?WT.mc_id=aiml-89446-dglover)"
      - "[Learn Module: Introduction to Azure OpenAI Service](https://learn.microsoft.com/training/modules/explore-azure-openai?WT.mc_id=aiml-89446-dglover)"
      - "[Case Study: Making generative AI training simple and cost-efficient with PeriFlow and Azure](https://startups.microsoft.com/blog/making-generative-ai-training-simple?WT.mc_id=aiml-89446-dglover)"


    - folder: "2023-04-04-openai-playground"
      emoji: 🏁
      audience: "Azure AI Developers"
      title: "Explore the Azure OpenAI Playground"
      description: "Explore Conversational AI with the Azure OpenAI Service Playground"
      authors: [Valentina]
      keywords: [Azure-OpenAI-Services, Azure-AI]
      tags: [azure-ai, azure-open-ai, 30-days-of-azure-ai]
      social_tag: "#OpenAI"
      canonical: https://medium.com/microsoftazure/azure-openai-playground-279f1f3da562
      references:
      - "[Azure OpenAI Service](https://azure.microsoft.com/products/cognitive-services/openai-service?WT.mc_id=aiml-89446-dglover)"
      - "[Learn Module: Introduction to Azure OpenAI Service](https://learn.microsoft.com/training/modules/explore-azure-openai?WT.mc_id=aiml-89446-dglover)"
      - "[Case Study: Azure OpenAI Service powers the next generation of startups](https://startups.microsoft.com/blog/azure-openai-service-for-startups?WT.mc_id=aiml-89446-dglover)"


    - folder: "2023-04-05-copilot-form-recognizer"
      emoji: 🏁
      audience: "Azure AI Developers"
      title: "Build an AI receipts app with Copilot"
      description: "Learn how to use Copilot to build an intelligent receipts app powered by Azure Form Recognizer"
      authors: [Ruth]
      keywords: [Form-Recognizers, Azure-Applied-AI-Services, CoPilot, vscode, Azure-AI]
      tags: [azure-ai, azure-cognitive-services, 30-days-of-azure-ai]
      social_tag: "#AzureCognitiveServices"
      canonical: https://techcommunity.microsoft.com/t5/ai-cognitive-services-blog/how-copilot-helps-developers-generate-code-for-a-form-recognizer/ba-p/3753813
      references:
        - "[What is Azure Form Recognizer?](https://learn.microsoft.com/azure/applied-ai-services/form-recognizer/overview?view=form-recog-3.0.0&WT.mc_id=aiml-89446-dglover)"
        - "[Learn Module: Learn about Azure Cognitive Services](https://learn.microsoft.com/training/browse/?products=azure-cognitive-services&WT.mc_id=aiml-89446-dglover)"
        - "[Learn Module: Introduction to Form Recognizer](https://learn.microsoft.com/training/modules/intro-to-form-recognizer?WT.mc_id=aiml-89446-dglover)"
        - "[Introducing GitHub Copilot: your AI pair programmer](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer?WT.mc_id=aiml-89446-dglover)"
        - "[Case Study: How Qard went from idea to MVP](https://startups.microsoft.com/blog/qard-idea-to-mvp?WT.mc_id=aiml-89446-dglover)"
```

## Usage

Run the generator.py script to generate the blog posts. It will create a folder for each day in the output directory.

1. The generator will validate the blog.yaml file and will fail if the file is not valid.
1. Pass the generator the path to the Docusaurus website folder and the content folder name.

    - -w is the path to the Docusaurus website folder. For example, /Users/dave/GitHub/AzureAiDevelopers/hub/website
    - -c is the content folder name. For example, 2023-aia

1. Blog items are stored in the `website/<content_name>` folder.
1. Blog item banners are stored in the `website/static/img/<content_name>` folder.

```bash
python3 generator.py -w "/Users/dave/GitHub/AzureAiDevelopers/hub/website" -c "2023-aia"
```

### Optional parameters


If you wish to update a blog item, then specify the folder name defined in the blogs.yaml file.

```bash
python3 generator.py -f "2023-04-04-openai-playground"
```

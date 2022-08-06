import os
from this import s
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEYS

def generateBlogIdeas(topic,Keywords):
    blog_topics = []
    response = openai.Completion.create(
        
        engine="text-davinci-002",
        prompt="Generate blog topic ideas on the following topic:{}\nKeywords: {}\n*" .format(topic,Keywords),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0 )

    if 'choices' in response:
        if len(response['choices']) >0:
            res = response['choices'][0]['text']
        else:
            return []
    else:
        return []
    a_list = res.split('*')
    if len(a_list) > 0:
        for blog in a_list:
            blog_topics.append(blog)
    else:
        return []
    return blog_topics
    

# def generateBlogSection(topic,keywords):
#     # blog_topics = []
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt="Generate blog section heading and section title, based on the following blog section.\nTopic:{}\nKeywords: {}\n* " .format(topic,keywords),
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         best_of=1,
#         frequency_penalty=0,
#         presence_penalty=0 )

#     if 'choices' in response:
#         if len(response['choice']) >0:
#             res = response['choices'][0]['text']
#         else:
#             res = None
#     else:
#         res = None
#     # a_list = res.split('*')
#     # if len(a_list) > 0:
#     #     for blog in a_list:
#     #         blog_topics.append(blog)
#     # else:
#     #     return []
#     return res

def generateBlogSectionHeadings(topic,Keywords):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate blog section heading and section title, based on the following blog section.\nTopic:{}\nKeywords: {}\n* " .format(topic,Keywords),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0 )

    if 'choices' in response:
        if len(response['choices']) >0:
            res = response['choices'][0]['text']
        else:
            res = None
    else:
        res = None
    return res

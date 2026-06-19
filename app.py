app.pyimport os
import requests

def ask_gemini(prompt):
    url = f"https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer anon", 
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Respond in Arabic."},
            {"role": "user", "content": prompt}
        ]
    }
    
    print("⏳ جاري التفكير وتوليد الإجابة...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "حدث خطأ في الاتصال، تأكد من الإنترنت."

if __name__ == "__main__":
    print("=== مرحبا بك في أداة الذكاء الاصطناعي الخاصة بك ===")
    user_input = input("اكتب سؤالك أو الفكرة التي تريد تشكيلها: ")
    
    ai_response = ask_gemini(user_input)
    print("\n=== رد الذكاء الاصطناعي ===")
    print(ai_response)

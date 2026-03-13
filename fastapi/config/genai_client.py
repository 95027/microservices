from google import genai
from config.settings import settings

client = genai.Client(api_key=settings.GOOGLE_GEMINI_API_KEY)


def generate_text(prompt: str):
    if not prompt:
        raise ValueError("Prompt cannot be Empty")
    
    res = client.models.generate_content(model="models/gemini-2.5-flash", contents=prompt)
    
    if res.candidates:
        candidate = res.candidates[0].content.parts[0]
        text = getattr(candidate, "text", "")
        finish_reason = getattr(candidate, "finish_reason", "UNKNOWN")
    else:
        text = ""
        finish_reason = "UNKNOWN"

    structured = {
        "text": text,
        "model": getattr(res, "model_version", "unknown"),
        "tokens_used": getattr(res.usage_metadata, "total_token_count", 0),
        "finish_reason": finish_reason
    }
    
    return structured
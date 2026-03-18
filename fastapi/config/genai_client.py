from google import genai
from config.settings import settings
import base64

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

def generate_audio_text(audio_bytes: bytes, prompt: str, mime_type: str):
    
    if not audio_bytes:
        raise ValueError("Audio bytes cannot be empty")
    
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    
    default_instruction = (
        "You are an AI assistant. "
        "Listen to the following audio input from the user and respond appropriately. "
        "Do not just transcribe it. "
        "If the audio contains a question, answer it. "
        "If it contains a request, follow it. "
        "If it is a statement, respond naturally and contextually."
    )
    
    instruction_text = prompt if prompt else default_instruction
    
    res = client.models.generate_content(
          model="models/gemini-2.5-flash",
          contents=[
              {
                  "role": "user",
                  "parts": [
                     {"text": instruction_text },
                      {
                          "inline_data": {
                              "mime_type": mime_type,
                              "data": audio_base64
                          }
                      }
                  ]
              }
          ]
    )
    
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
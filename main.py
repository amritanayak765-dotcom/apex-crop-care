from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="APEX Crop Care API")

# Browser aur Frontend communication allow karne ke liye CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "APEX Python FastAPI Server Active"}

# AI Diagnostic Model Endpoint (PPT Slide 3 & 4)
@app.post("/api/diagnose")
async def diagnose_crop(file: UploadFile = File(...)):
    # PyTorch/TensorFlow CNN inference simulation
    confidence_score = random.randint(75, 98)
    diseases = ["Early Blight", "Leaf Rust", "Powdery Mildew", "Healthy Crop"]
    detected_disease = random.choice(diseases)
    
    # PPT Slide 4: Low confidence (<85%) auto-routes to KVK experts
    routed_to_kvk = confidence_score < 85

    return {
        "filename": file.filename,
        "disease": detected_disease,
        "confidence": confidence_score,
        "advisory": "Organic copper spray apply karein. Hawa kam hone par hi chidkaav karein.",
        "routed_to_kvk_expert": routed_to_kvk
    }

# Pesticide & Water Dosage Calculator Endpoint (PPT Slide 3)
@app.get("/api/dosage")
def calculate_dosage(acres: float, disease_type: str):
    water_required = acres * 200  # 200 Liters per acre
    
    if disease_type == "blight":
        chemical_required = acres * 400
    elif disease_type == "rust":
        chemical_required = acres * 500
    else:
        chemical_required = acres * 250

    return {
        "acres": acres,
        "water_liters": water_required,
        "chemical_grams": chemical_required
    }

import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
    
    

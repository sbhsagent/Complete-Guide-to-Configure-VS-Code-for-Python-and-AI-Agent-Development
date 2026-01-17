import torch

print(f"✓ PyTorch version: {torch.__version__}")
print(f"✓ CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"✓ GPU device: {torch.cuda.get_device_name(0)}")
    print(f"✓ CUDA version built with: {torch.version.cuda}")
    print(f"✓ Number of GPUs: {torch.cuda.device_count()}")

    # Test tensor operation
    try:
        x = torch.rand(5, 3).cuda()
        print(f"✓ Tensor operation successful: {x.mean()}")
    except RuntimeError as e:
        print(f"✗ CUDA operation failed: {str(e)}")
        print("Common solutions: Reinstall CUDA drivers or use torch==2.7.0+cu121")
# Add a check for Apple Silicon (MPS)
elif torch.backends.mps.is_available():
    print(f"✓ Apple Silicon MPS available")
    print(f"✓ Using device: mps")
else:
    print("ℹ️ No GPU detected - using CPU only")

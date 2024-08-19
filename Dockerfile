# Use the official PyTorch image from Docker Hub as the base image
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

# Set the working directory inside the container
WORKDIR /workspace

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set an environment variable to avoid potential issues with OpenMP
ENV OMP_NUM_THREADS=1

# Default command to run when the container starts
CMD ["bash"]

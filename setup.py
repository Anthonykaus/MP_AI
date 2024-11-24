from setuptools import setup, find_packages

setup(
    name='manhattan_project_for_ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.4.0',
        'torch>=1.8.0',
        'onnx>=1.9.0',
        'numpy>=1.19.0',
        'scipy>=1.6.0',
        'matplotlib>=3.3.0',
        'pandas>=1.2.0',
        'transformers>=4.5.0',
        'deap>=1.3.1',
        'stable-baselines3>=1.0.0',
        'ray[default]>=1.6.0',
    ],
    entry_points={
        'console_scripts': [
            'mpai-train=training.local_training_pipeline:main',
            'mpai-generate-code=code_generation.transformer_based_codegen:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='The Manhattan Project for AI: A Fully Autonomous AI Model and System.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Anthonykaus/manhattan_project_for_ai.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

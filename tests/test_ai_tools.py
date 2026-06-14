"""Tests for AI/ML tooling detection."""
from __future__ import annotations

import json

from atlas.detector import detect_ai_models, detect_ai_tools


class TestPythonAIDeps:
    def test_anthropic(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("anthropic==0.40.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "Anthropic SDK" in tools

    def test_openai(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("openai>=1.0.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "OpenAI SDK" in tools

    def test_langchain(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("langchain>=0.1.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "LangChain" in tools

    def test_llama_index(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("llama-index>=0.10.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "LlamaIndex" in tools

    def test_transformers(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("transformers>=4.30.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "Transformers" in tools

    def test_pytorch(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("torch>=2.0.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "PyTorch" in tools

    def test_tensorflow(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("tensorflow>=2.15.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "TensorFlow" in tools

    def test_scikit_learn(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("scikit-learn>=1.3.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "scikit-learn" in tools

    def test_mlflow(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("mlflow>=2.0.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "MLflow" in tools

    def test_wandb(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("wandb>=0.16.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "Weights & Biases" in tools

    def test_chromadb(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("chromadb>=0.4.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "ChromaDB" in tools

    def test_pinecone(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("pinecone-client>=3.0.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "Pinecone" in tools

    def test_sentence_transformers(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("sentence-transformers>=2.0.0\n")
        tools = detect_ai_tools(tmp_path)
        assert "Sentence Transformers" in tools

    def test_pyproject_toml(self, tmp_path):
        (tmp_path / "pyproject.toml").write_text(
            '[project]\ndependencies = ["anthropic>=0.40", "langchain"]\n'
        )
        tools = detect_ai_tools(tmp_path)
        assert "Anthropic SDK" in tools
        assert "LangChain" in tools

    def test_no_ai_deps(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("fastapi>=0.109.0\nrich>=13.0\n")
        tools = detect_ai_tools(tmp_path)
        assert tools == []


class TestJavaScriptAIDeps:
    def test_anthropic_js(self, tmp_path):
        pkg = {"dependencies": {"@anthropic-ai/sdk": "^0.30.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "Anthropic SDK" in tools

    def test_openai_js(self, tmp_path):
        pkg = {"dependencies": {"openai": "^4.0.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "OpenAI SDK" in tools

    def test_langchain_js(self, tmp_path):
        pkg = {"dependencies": {"@langchain/core": "^0.2.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "LangChain" in tools

    def test_vercel_ai_sdk(self, tmp_path):
        pkg = {"dependencies": {"ai": "^3.0.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "Vercel AI SDK" in tools

    def test_vercel_ai_anthropic(self, tmp_path):
        pkg = {"dependencies": {"@ai-sdk/anthropic": "^0.1.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "Vercel AI SDK" in tools

    def test_huggingface_js(self, tmp_path):
        pkg = {"dependencies": {"@huggingface/inference": "^2.0.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert "Hugging Face" in tools

    def test_no_ai_js_deps(self, tmp_path):
        pkg = {"dependencies": {"next": "^14.0.0", "react": "^18.0.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert tools == []


class TestJupyterNotebooks:
    def test_notebook_detected(self, tmp_path):
        (tmp_path / "analysis.ipynb").write_text('{"cells": []}')
        tools = detect_ai_tools(tmp_path)
        assert "Jupyter" in tools

    def test_no_notebooks(self, tmp_path):
        (tmp_path / "main.py").write_text("print('hello')")
        tools = detect_ai_tools(tmp_path)
        assert "Jupyter" not in tools

    def test_notebook_in_subdir(self, tmp_path):
        nb_dir = tmp_path / "notebooks"
        nb_dir.mkdir()
        (nb_dir / "train.ipynb").write_text('{"cells": []}')
        tools = detect_ai_tools(tmp_path)
        assert "Jupyter" in tools


class TestMLInfraFiles:
    def test_mlproject(self, tmp_path):
        (tmp_path / "MLproject").write_text("name: myproject")
        tools = detect_ai_tools(tmp_path)
        assert "MLflow" in tools

    def test_wandb_dir(self, tmp_path):
        (tmp_path / "wandb").mkdir()
        tools = detect_ai_tools(tmp_path)
        assert "Weights & Biases" in tools

    def test_dvc_yaml(self, tmp_path):
        (tmp_path / "dvc.yaml").write_text("stages:\n  train:\n    cmd: python train.py")
        tools = detect_ai_tools(tmp_path)
        assert "DVC" in tools

    def test_dvc_dir(self, tmp_path):
        (tmp_path / ".dvc").mkdir()
        tools = detect_ai_tools(tmp_path)
        assert "DVC" in tools


class TestEmptyProject:
    def test_empty_dir(self, tmp_path):
        tools = detect_ai_tools(tmp_path)
        assert tools == []

    def test_combined_ai_stack(self, tmp_path):
        """A project with multiple AI tools."""
        (tmp_path / "requirements.txt").write_text(
            "anthropic>=0.40.0\nlangchain>=0.1.0\nchromadb>=0.4.0\n"
        )
        (tmp_path / "train.ipynb").write_text('{"cells": []}')
        tools = detect_ai_tools(tmp_path)
        assert "Anthropic SDK" in tools
        assert "LangChain" in tools
        assert "ChromaDB" in tools
        assert "Jupyter" in tools
        assert len(tools) == 4

    def test_no_duplicate_from_python_and_js(self, tmp_path):
        """Same tool in Python and JS deps should not duplicate."""
        (tmp_path / "requirements.txt").write_text("openai>=1.0.0\n")
        pkg = {"dependencies": {"openai": "^4.0.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))
        tools = detect_ai_tools(tmp_path)
        assert tools.count("OpenAI SDK") == 1


class TestDetectAIModels:
    def test_detects_claude_model_in_python(self, tmp_path):
        (tmp_path / "client.py").write_text('MODEL = "claude-opus-4-8"\n')
        assert "claude-opus-4-8" in detect_ai_models(tmp_path)

    def test_detects_openai_model_in_typescript(self, tmp_path):
        (tmp_path / "agent.ts").write_text('const model = "gpt-4o-mini";\n')
        assert "gpt-4o-mini" in detect_ai_models(tmp_path)

    def test_detects_dated_anthropic_id(self, tmp_path):
        (tmp_path / "cfg.py").write_text('m = "claude-3-5-sonnet-20241022"\n')
        assert "claude-3-5-sonnet-20241022" in detect_ai_models(tmp_path)

    def test_detects_gemini_and_mistral(self, tmp_path):
        (tmp_path / "providers.py").write_text(
            'A = "gemini-2.0-flash"\nB = "mixtral-8x7b"\n'
        )
        models = detect_ai_models(tmp_path)
        assert "gemini-2.0-flash" in models
        assert "mixtral-8x7b" in models

    def test_detects_in_env_and_toml(self, tmp_path):
        (tmp_path / ".env.example").write_text("OPENAI_MODEL=gpt-4o\n")
        (tmp_path / "config.toml").write_text('model = "claude-sonnet-4-6"\n')
        models = detect_ai_models(tmp_path)
        assert "gpt-4o" in models
        assert "claude-sonnet-4-6" in models

    def test_returns_sorted_and_deduped(self, tmp_path):
        (tmp_path / "a.py").write_text('"gpt-4o" "gpt-4o" "claude-opus-4-8"\n')
        models = detect_ai_models(tmp_path)
        assert models == sorted(set(models))
        assert models.count("gpt-4o") == 1

    def test_ignores_test_files(self, tmp_path):
        # Test fixtures enumerate models — would create false drift
        tdir = tmp_path / "tests"
        tdir.mkdir()
        (tdir / "test_models.py").write_text('"gpt-3.5-turbo" "claude-instant-1.2"\n')
        (tmp_path / "main.py").write_text('"gpt-4o"\n')
        models = detect_ai_models(tmp_path)
        assert "gpt-4o" in models
        assert "gpt-3.5-turbo" not in models

    def test_ignores_docs_markdown(self, tmp_path):
        # Docs are mentions, not pins
        (tmp_path / "README.md").write_text("We considered gpt-4o and claude-opus-4-8.\n")
        assert detect_ai_models(tmp_path) == []

    def test_no_false_positive_on_bogus_version(self, tmp_path):
        # 'claude-1000' is not a real model family — must not match
        (tmp_path / "x.py").write_text('label = "claude-1000-internal-id"\n')
        assert detect_ai_models(tmp_path) == []

    def test_does_not_match_bare_words(self, tmp_path):
        (tmp_path / "prose.py").write_text("# we use claude and gpt here\n")
        assert detect_ai_models(tmp_path) == []

    def test_skips_large_files(self, tmp_path):
        big = tmp_path / "huge.py"
        big.write_text("x = 1\n" * 100 + '"gpt-4o"\n' + "y = 2\n" * 200_000)
        assert big.stat().st_size > 512 * 1024
        assert detect_ai_models(tmp_path) == []

    def test_ignores_bulk_data_json(self, tmp_path):
        # .json admitted only by config-ish name, not arbitrary data dumps
        (tmp_path / "data-0001.json").write_text('{"note": "gpt-4o"}\n')
        assert detect_ai_models(tmp_path) == []
        (tmp_path / "model.config.json").write_text('{"model": "gpt-4o"}\n')
        assert "gpt-4o" in detect_ai_models(tmp_path)

    def test_empty_project(self, tmp_path):
        (tmp_path / "main.py").write_text("print('hello')\n")
        assert detect_ai_models(tmp_path) == []

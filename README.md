**IT5005 — CLIP and LoRA Project**

This repository contains the two IT5005 project notebooks and a shared Poetry environment for local development.

- **Part 1:** CLIP zero-shot classification, prompt comparisons and a trained classification head on ImageNet features.
- **Part 2:** Image–text retrieval on Flickr8k using projection-only fine-tuning and LoRA.

The notebooks are starter templates with implementation and written-answer TODOs. Setting up the environment prepares them for development; the group still needs to complete the assignment.

Read the [project brief](IT5005_Project_August_2026.pdf) and the [work allocation and proposed schedule](WORK_ALLOCATION.md) for the four-member team.

**Get started**

Install Git, **Python 3.12** and **Poetry 2.2.1 or later**. Poetry installation instructions are available in the [official documentation](https://python-poetry.org/docs/#installation). A Conda environment is not required.

Clone the repository and run all subsequent commands from its root:

```bash
git clone https://github.com/sbhhbs/IT5005_CLIP_LORA.git
cd IT5005_CLIP_LORA
poetry env use python3.12
poetry install
poetry env info --path
```

The last command should show this repository's `.venv` directory. The committed `poetry.toml` configures that location. Keep other virtual environments deactivated when creating it. If `python3.12` is not on your PATH, pass the full path to the Python 3.12 executable to `poetry env use`; on Windows, `py -3.12 -c "import sys; print(sys.executable)"` can locate it.

`pyproject.toml` declares the dependencies and `poetry.lock` records their resolved versions. `project_requirements.txt` preserves the supplied dependency list for reference. The environment also includes `peft` for the optional comparison. Use `poetry install` for onboarding and after pulling dependency changes; coordinate dependency updates and commit both Poetry files together.

**Open the notebooks**

```bash
poetry run jupyter notebook
```

Open `Part_1.ipynb` or `Part_2.ipynb`. Keep the notebook working directory at the repository root so relative paths find `id_to_label.json` and the caches.

For VS Code or another Jupyter installation, register the environment as a named kernel:

```bash
poetry run python -m ipykernel install --user --name it5005-clip-lora --display-name "Python (IT5005 CLIP LoRA)"
```

Select **Python (IT5005 CLIP LoRA)** in the notebook kernel picker, or select this repository's `.venv` interpreter. Confirm the selected Python from a scratch cell:

```python
import sys
print(sys.version)
print(sys.executable)
```

It should report Python 3.12 and a path inside `.venv`. The notebooks select CUDA when available, then Apple MPS, then CPU. Check the printed device rather than assuming GPU use. NVIDIA users may need a compatible PyTorch build for their system; agree any dependency/source changes with the group.

**Caching and local runs**

| Location | Purpose |
|---|---|
| `cache/imagenet_val_clip/` | Part 1 image features and labels |
| `cache_part2/vision_pooled.pt` | Part 2 frozen image-encoder features |
| `cache_part2/text_pooled.pt` | Part 2 frozen text-encoder features |
| `runs/` | TensorBoard logs |

Part 1's first encoding pass covers 50,000 images and can take an hour or more on CPU. Validate `encode_image` first, keep the computer powered and awake, and retain the completed cache. Later runs reuse it. This initial pass saves only when encoding finishes, so it cannot resume an interrupted partial run.

Cache files are not automatically invalidated when code changes. Rebuild affected caches when the encoder, preprocessing or dataset changes. Share complete caches through the group's file-sharing folder with the generating Git commit, model/dataset identifiers and package versions. Part 2 features must match the exact dataset row order. Extract shared caches locally before running.

Part 2's LoRA runs compute text-encoder outputs live while reusing frozen image features. The current `checkpoints` dictionary and training histories are primarily in memory: saving an `.ipynb` saves displayed outputs, not the trained model state. Disk checkpoint export/resume is not implemented. Run the integrated experiment sequence in one kernel, or agree explicit state/configuration exports before attempting a handoff between machines.

To inspect training logs:

```bash
poetry run tensorboard --logdir runs
```

**How we collaborate**

- **A + C own Part 1.** A leads encoder/probe implementation and final integration; C owns prompt/similarity experiments and paper answers.
- **B + D own Part 2.** B leads losses, metrics, LoRA, trainer and final integration; D owns setup/data preparation, experiments and results analysis.
- **Bob coordinates the presentation and processes the video.** Each member prepares their assigned slides and recording.

Pull the latest changes, create a task branch, and submit a small pull request describing the cells changed and checks performed. A reviews Part 1 changes; B reviews Part 2 changes. Agree notebook editing handoffs within each pair: simultaneous edits can conflict through outputs and metadata even when the code cells differ. Use scratch notebooks for overlapping development, then integrate the intended cells.

Choose one primary run machine per part. Share result tables, plots, settings and the generating commit after each experiment stage. Select prompts and hyperparameters using validation data; use test data for the final comparison and subsequent qualitative examples.

Git tracks notebooks, dependency files, labels and documentation. `.venv`, caches, logs, model weights and videos are ignored; share those separately. Preserve outputs in the final submission notebooks.

**Submission**

The brief specifies **Tuesday, 17 November 2026**; check Canvas for the exact cutoff time.

The proposed three-week schedule is:

| Dates | Focus |
|---|---|
| **27 October–2 November** | A and B finish core coding; C and D read the papers and complete the assigned prompt/setup preparation. |
| **3–9 November** | Evaluation, results analysis and completion of the written notebook questions. |
| **10–16 November** | Slides, rehearsal and video recording; Bob assembles and checks the video, and the group checks the final notebooks. |

1. Complete all implementation and written-answer cells, group details and both AI Usage tables.
2. Restart each kernel, run all cells in order, and save the outputs.
3. Submit `group_<id>_part_1.ipynb`, `group_<id>_part_2.ipynb`, and `group_<id>_video.mp4` or a viewable link in `group_<id>_video.txt`.
4. Exclude cache folders and the environment from submission. Written answers belong in the notebooks; there is no separate PDF report.

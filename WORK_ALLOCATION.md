**IT5005 Project — Work Allocation**

This allocation uses two working pairs: **A and C for Part 1**, and **B and D for Part 2**. A and B lead the core implementation for their respective parts. C owns Part 1 experiments and analysis; D owns Part 2 setup, experiments and results analysis.

**Cell numbering:** References count every Markdown and code cell from **1** at the title cell in the supplied notebooks. They are cell positions, not execution numbers such as `In [8]`. Use the question/step and function names if cells are subsequently inserted or removed.

| Member | Role | Main deliverables | Video questions |
|---|---|---|---|
| A | Part 1 implementation lead | Encoder, ImageNet feature preparation, probe training and analysis; final Part 1 notebook | Q1, Q2, Q5 |
| B | Part 2 implementation lead | Contrastive losses, Recall@K, LoRA and trainer; technical analysis; final Part 2 notebook | Q6, Q8, Q9 |
| C | Part 1 experiments and analysis | Prompt/similarity implementation and experiments; paper answers; support for Part 1 integration | Q3, Q4, Q12 |
| D | Part 2 setup, experiments and analysis | Model/data setup; experiment execution; methodology, final results and qualitative analysis | Q7, Q10, Q11 |

**Proposed schedule**

The proposed plan allocates one week to coding and paper reading, one week to evaluation and written answers, and one week to video preparation and recording. Dates assume a start on **27 October 2026**.

| Week | Dates | Focus | Expected outcome |
|---|---|---|---|
| 1 | 27 October–2 November | A and B finish the core coding for Parts 1 and 2. C and D read the relevant papers and prepare their assigned prompt/setup cells alongside the reading. | Integrated implementations and required preparation are ready for evaluation. |
| 2 | 3–9 November | Run the evaluations, compare results and complete all written notebook questions. A and B resolve implementation issues with C and D. | Saved results, plots and completed answers are ready for the presentation. |
| 3 | 10–16 November | Prepare slides and scripts, rehearse and record each member's video sections. Bob coordinates the presentation, assembles the recordings and checks the final video. | The video and final checked notebooks are ready for submission. |

**Submission:** Tuesday, **17 November 2026**, by the cutoff shown on Canvas. Complete the final checks during Week 3.

**Member A — Part 1 implementation lead**

| Done | Notebook location | Cells | Work and expected output |
|---|---|---|---|
| ☐ | Part 1, Q1, Steps 1–2 | 4, 6 | Run model setup and the demonstration image cell. Confirm the environment and device work. |
| ☐ | Part 1, Q1, Step 3 | 8 | Implement `CLIPEncoder.encode_image`, `encode_text` and `predict`. |
| ☐ | Part 1, Q1, Steps 4–5 and metrics | 10, 12, 14 | Run the encoder demonstration, build the ImageNet feature cache, and prepare train/validation/test features and metric helpers. Share the working setup with C. |
| ☐ | Part 1, Q3, Step 10 | 26 | Complete `ClsNetwork`, including LayerNorm, output layer and forward pass. |
| ☐ | Part 1, Q3, Step 11 | 28 | Complete the training step and trainer invocation. Train with the specified learning rate, maximum epochs and early stopping. |
| ☐ | Part 1, Q3, final evaluation and Step 12 | 30, 32 | After C supplies the zero-shot results, run final probe evaluation. Write the test accuracy/macro-F1 comparison and discuss data, flexibility and computational trade-offs. |

Video ownership: **Q1, Q2 and Q5**. Supply D with Part 1's validation-selection details for Q10, and B with the probe architecture and parameter count for Q8. Review C's Part 1 analyses and integrate the final Part 1 notebook.

**Member B — Part 2 implementation lead**

| Done | Notebook location | Cells | Work and expected output |
|---|---|---|---|
| ☐ | Part 2, Step 5 | 21–23 | Review the provided `RetrievalCLIP` wrapper, implement `info_nce_loss` and `triplet_loss` in cell 22, and pass the supplied checks. |
| ☐ | Part 2, Step 6 | 25–27 | Implement `recall_at_k`, verify compatibility with the evaluation helpers, and pass the retrieval checks. |
| ☐ | Part 2, Step 7 | 29, 30, 32 | Implement `LoRALinear.__init__`, `forward` and `merge`; pass the supplied checks; verify integration with the provided injection/setup functions. |
| ☐ | Part 2, Step 8 | 35 | Complete the training step. Verify gradient updates, validation evaluation and restoration of the selected checkpoint. Integrate with D's model and data setup. |
| ☐ | Part 2, Step 9.9, Q2 | 57 | Write the InfoNCE-versus-triplet analysis using the actual loss and validation curves. |
| ☐ | Part 2, Step 9.9, Q5 | 63 | Write the LoRA parameter derivation, rank comparison, timing discussion, initialization explanation and merge analysis. Compare ranks using validation results; report test recall for the selected rank. |
| ☐ | Part 2, experiment support | 38–52, code cells | Resolve implementation issues during D's experiment runs. Review loss, parameter-count and merging evidence, and check the methodology and results interpretations with D. |
| ☐ | Part 2, integration | All required cells | Integrate D's setup, experiment outputs and answer cells; complete the final notebook run with all outputs saved. |

Video ownership: **Q6, Q8 and Q9**. Prepare a printed four-pair example from the group's InfoNCE implementation. Obtain probe details from A for Q8 and rank-sweep, parameter-count and merge outputs from D for Q9. Review the loss-comparison explanation with D for Q7.

**Member C — Part 1 experiments and analysis**

| Done | Notebook location | Cells | Work and expected output |
|---|---|---|---|
| ☐ | Part 1, Q2, Step 6 | 17 | Implement `evaluate_zero_shot_prompts`, add at least two original prompt templates, and record validation accuracy for every template. |
| ☐ | Part 1, Q2, Step 7 | 19 | Write the prompt comparison and explain the effect of the unrelated prefix. |
| ☐ | Part 1, Q2, Step 8 | 21 | Select the prompt programmatically from validation results, evaluate dot-product and cosine accuracy on the test set, and inspect embedding norms. Share results with A. |
| ☐ | Part 1, Q2, Step 9 | 23 | Write the similarity analysis, including when rankings coincide and how vector norms affect class rankings. |
| ☐ | Part 1, Q4.1–Q4.5 | 35, 37, 39, 41, 43 | Answer the five paper questions: what CLIP learns, contrastive learning, generalization, label construction and limitations. |

Video ownership: **Q3, Q4 and Q12**. Use the Part 1 paper analysis and the retrieval examples supplied by D for the limitations discussion. Review claims about projection-only tuning and LoRA with B, and explain possible regressions after Flickr8k tuning and how they could be tested. C's notebook ownership is entirely in Part 1; the final limitations question draws on both parts.

**Member D — Part 2 setup, experiments and analysis**

| Done | Notebook location | Cells | Work and expected output |
|---|---|---|---|
| ☐ | Part 2, Steps 1–2 | 3, 5, 7 | Run imports, load CLIP and its processor, and produce the parameter breakdown. |
| ☐ | Part 2, Step 3 | 9, 10 | Implement `setup_projection_peft` and pass the freezing/trainable-parameter checks. |
| ☐ | Part 2, Step 4.1 | 13, 14 | Implement `load_and_split_dataset` and verify the dataset split. |
| ☐ | Part 2, Steps 4.2–4.3 | 16, 18, 19 | Run feature caching, implement `FlickrFeatureDataset.__getitem__`, and verify the DataLoaders. Share the working setup with B for integration. |
| ☐ | Part 2, Steps 9.1–9.2 | 38, 40 | Once B's implementation is integrated, run the zero-shot baseline and projection-only InfoNCE/triplet experiments. Preserve validation results, histories and checkpoints. |
| ☐ | Part 2, Steps 9.3–9.4 | 42, 44 | Run the learning-rate sweep and 25-epoch diagnostic. Record the validation-selected learning rate and the patience-3 stopping epoch. |
| ☐ | Part 2, Step 9.5 | 46 | Run the LoRA rank experiments after Steps 9.1–9.4. Record validation recall, parameter counts and training time, then select rank using validation results. |
| ☐ | Part 2, Step 9.6 | 48 | Run the merge comparison and record validation metrics and timing before and after merging. |
| ☐ | Part 2, Step 9.7 | 50 | Once all choices are fixed, run the final test comparison for the selected model of each method. Share the final table with B and C. |
| ☐ | Part 2, Step 9.8 | 52 | After the final test comparison, run qualitative retrieval and select one successful and one unsuccessful example. Preserve the image/caption outputs and share them with C for video Q12. |
| ☐ | Part 2, Step 9.9, Q1 | 55 | Write the performance comparison across zero-shot, projection-only InfoNCE, projection-only triplet and LoRA, including both retrieval directions. |
| ☐ | Part 2, Step 9.9, Q3–Q4 | 59, 61 | Write the learning-rate and overfitting analyses, including validation-based selection and the early-stopping calculation. |
| ☐ | Part 2, Step 9.9, Q6 | 65 | Explain what the model got right and why the unsuccessful retrieval may have failed. |

Video ownership: **Q7, Q10 and Q11**. Use the loss/validation curves and final test recall for Q7, reviewing the explanation with B. Obtain Part 1 validation-selection details from A and C for Q10. Present the final Part 2 test table and discuss confidence in the comparisons for Q11.

The PEFT-library comparison in Part 2 cell 33 and image-side LoRA extension in cell 66 are optional and outside the required allocation.

**Video work list — present in this order**

The targets total **28 minutes**, leaving **2 minutes** within the 30-minute limit for transitions and pacing. A, B and D have **7 minutes** each; C has **6 minutes 30 seconds**. The **30-second introduction** will be assigned separately; its speaker is **TBD**.

| Order | Owner | Target | Content and evidence to prepare |
|---|---|---|---|
| Introduction | TBD | 0:30 | Group members, project goal and presentation outline. |
| Q1 — Architecture | A | 2:30 | Trace image patches and caption tokens through CLIP ViT-B/32, the selected output tokens, projections, normalization and `logit_scale`. Explain why projections are needed. Show model/feature outputs from Part 1 Q1; add a shape or scale printout if needed. |
| Q2 — Zero-shot classifier | A | 2:00 | Walk through `encode_image`, `encode_text` and `predict`; explain how 1,000 class names form a classifier. Show Part 1 cells 8, 10 and the class-prompt outputs from C. |
| Q3 — Similarity measure | C | 2:00 | Show Part 1 cell 21 accuracies and embedding norms. Explain when rankings coincide and which vector norms can change class rankings without normalization. |
| Q4 — Prompts | C | 2:00 | Show the validation prompt table from cell 17. Discuss the best prompts, whether the differences are meaningful, the unrelated prefix and the 77-token limit. |
| Q5 — Probe vs. zero-shot | A | 2:30 | Show Part 1 cell 30 test results, identify the validation-selected epoch, and explain performance and trade-offs using cell 32. |
| Q6 — InfoNCE | B | 2:00 | Explain four image-caption pairs: positives, negatives, labels, both directions and temperature. Show a printed four-pair example from the group's loss implementation. |
| Q7 — InfoNCE vs. triplet | D | 2:00 | Show Part 2 cell 40 curves and cell 50 final recall. Explain the difference in how negatives are used, using B's loss analysis. |
| Q8 — Fine-tuning strategies | B | 2:00 | Compare the probe, projection-only tuning and LoRA: trained components, parameter counts and what can change. Show a comparison table derived from the group's models. |
| Q9 — LoRA | B | 3:00 | Explain the equation, A/B shapes, parameter count for rank 8, zero initialization of B and merging. Show rank-sweep outputs from cell 46 and merge results from cell 48. |
| Q10 — Methodology | D | 3:00 | Explain validation-based choices in both parts. Show learning-rate and 25-epoch curves from cells 42 and 44; identify underfitting/overfitting where supported and the patience-3 stopping epoch. |
| Q11 — Results | D | 2:00 | Show Part 2 cell 50 final test table. State the main finding and discuss confidence given test-set size and run-to-run variation. Distinguish measured variation from uncertainty that was not measured. |
| Q12 — Limitations | C | 2:30 | Show a retrieval failure from cell 52. Explain CLIP's limitations, limits of projection-only tuning and LoRA, possible regressions after Flickr8k tuning, and how to test them. |

All members state their names when they start speaking. Use screen recording with voice-over and webcam. Every checkpoint answer must refer to the group's own printed results, plots or tables. Bob coordinates the presentation and processes the final video.

**Handoffs and execution order**

1. **Initial parallel work:** A develops Part 1's encoder, feature preparation and probe. C starts paper reading and prompt templates. B develops Part 2's losses, metrics, LoRA and trainer in Steps 5–8. D implements Part 2 setup and data preparation in Steps 1–4.
2. **Part 1 handoff:** A supplies the working encoder and feature setup to C. C supplies `best_prompt`, `accuracy_dot`, `accuracy_cos` and prompt/norm outputs to A for the final probe comparison. A integrates the final Part 1 notebook.
3. **Part 2 implementation handoff:** D supplies the working model/data setup to B. B integrates Steps 1–8, verifies the provided checks with D and supplies a working notebook for the experiments. B owns fixes to the losses, metrics, LoRA and trainer; D owns fixes to the setup and data preparation, with B reviewing integration.
4. **Part 2 experiment sequence:** D runs cells **38 → 40 → 42 → 44 → 46 → 48 → 50 → 52** in order, with B providing implementation support. Use one integrated notebook in the same live kernel: histories, checkpoints, `BEST_LR` and the selected `lora_model` are held in memory. Saved notebook outputs alone do not transfer this state between computers. B owns the final integrated notebook run after D's outputs and answers are incorporated.
5. **Evaluation:** Select prompts, learning rates, epochs and LoRA rank using validation data. Fix those choices before final test evaluation. Use test results for reporting and subsequent illustrative retrieval examples; do not use them to revise the selected settings.
6. **Analysis and recording:** D shares all Part 2 curves, tables, timing and merge outputs with B for the technical answers and video, and supplies retrieval examples to C for Q12. A and C supply Part 1 validation-selection details to D for Q10. Each member completes their answer cells, prepares their assigned video sections and supplies slides/recordings to Bob.

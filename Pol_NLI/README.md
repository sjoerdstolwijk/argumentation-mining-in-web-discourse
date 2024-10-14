---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: entailment
    dtype: int64
  - name: dataset
    dtype: string
  - name: task
    dtype: string
  - name: augmented_hypothesis
    dtype: string
  splits:
  - name: train
    num_bytes: 92356849
    num_examples: 171289
  - name: validation
    num_bytes: 7152373
    num_examples: 15036
  - name: test
    num_bytes: 6703882
    num_examples: 15366
  download_size: 40469685
  dataset_size: 106213104
task_categories:
- text-classification
- zero-shot-classification
language:
- en
pretty_name: PolNLI
size_categories:
- 100K<n<1M
---
# Dataset Card for "Pol_NLI"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)



### Citation

To cite the paper introducing this dataset, please use:

```bibtex
@misc{burnham2024politicaldebateefficientzeroshot,
      title={Political DEBATE: Efficient Zero-shot and Few-shot Classifiers for Political Text}, 
      author={Michael Burnham and Kayla Kahn and Ryan Yank Wang and Rachel X. Peng},
      year={2024},
      eprint={2409.02078},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.02078}, 
}
```
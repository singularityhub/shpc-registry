---
layout: container
name:  "quay.io/biocontainers/shannon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shannon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shannon/container.yaml"
updated_at: "2023-07-10 03:28:58.595424"
latest: "0.0.2--py_1"
container_url: "https://biocontainers.pro/tools/shannon"
aliases:
 - "algorithm_SF.py"
 - "dsdp5"
 - "ext_corr.py"
 - "extension_correction.py"
 - "extension_correction_Kminus1.py"
 - "fast_reps.py"
 - "faster_reps.py"
 - "filter_FP.py"
 - "filter_FP_2s.py"
 - "filter_kallisto.py"
 - "filter_trans.py"
 - "find_reps_blat.py"
 - "kmers_for_component.py"
 - "kmers_for_component_back.py"
 - "kp1mer_to_kmer.py"
 - "mbgraph.py"
 - "merge_mate_pairs"
 - "multibridging.py"
 - "parallel_blat.py"
 - "parallel_blat_python.py"
 - "path_decompose_sparse.py"
 - "process_concatenated_fasta.py"
 - "quorum"
 - "quorum_create_database"
 - "quorum_error_correct_reads"
 - "rc_gnu.py"
 - "rc_s.py"
 - "run_MB_SF.py"
 - "run_MB_SF_fn.py"
 - "run_parallel_cmds.py"
 - "run_quorum.py"
 - "shannon.py"
 - "split_mate_pairs"
 - "test.py"
 - "test_suite.py"
 - "tester.py"
 - "trie.py"
 - "weight_updated_graph.py"
 - "jellyfish"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
versions:
 - "0.0.2--py_1"
description: "shpc-registry automated BioContainers addition for shannon"
config: {"url": "https://biocontainers.pro/tools/shannon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shannon", "latest": {"0.0.2--py_1": "sha256:f726492df1c5e8580e76cc2aec5194247b0fca28ed7085086f14c0c3274d7b37"}, "tags": {"0.0.2--py_1": "sha256:f726492df1c5e8580e76cc2aec5194247b0fca28ed7085086f14c0c3274d7b37"}, "docker": "quay.io/biocontainers/shannon", "aliases": {"algorithm_SF.py": "/usr/local/bin/algorithm_SF.py", "dsdp5": "/usr/local/bin/dsdp5", "ext_corr.py": "/usr/local/bin/ext_corr.py", "extension_correction.py": "/usr/local/bin/extension_correction.py", "extension_correction_Kminus1.py": "/usr/local/bin/extension_correction_Kminus1.py", "fast_reps.py": "/usr/local/bin/fast_reps.py", "faster_reps.py": "/usr/local/bin/faster_reps.py", "filter_FP.py": "/usr/local/bin/filter_FP.py", "filter_FP_2s.py": "/usr/local/bin/filter_FP_2s.py", "filter_kallisto.py": "/usr/local/bin/filter_kallisto.py", "filter_trans.py": "/usr/local/bin/filter_trans.py", "find_reps_blat.py": "/usr/local/bin/find_reps_blat.py", "kmers_for_component.py": "/usr/local/bin/kmers_for_component.py", "kmers_for_component_back.py": "/usr/local/bin/kmers_for_component_back.py", "kp1mer_to_kmer.py": "/usr/local/bin/kp1mer_to_kmer.py", "mbgraph.py": "/usr/local/bin/mbgraph.py", "merge_mate_pairs": "/usr/local/bin/merge_mate_pairs", "multibridging.py": "/usr/local/bin/multibridging.py", "parallel_blat.py": "/usr/local/bin/parallel_blat.py", "parallel_blat_python.py": "/usr/local/bin/parallel_blat_python.py", "path_decompose_sparse.py": "/usr/local/bin/path_decompose_sparse.py", "process_concatenated_fasta.py": "/usr/local/bin/process_concatenated_fasta.py", "quorum": "/usr/local/bin/quorum", "quorum_create_database": "/usr/local/bin/quorum_create_database", "quorum_error_correct_reads": "/usr/local/bin/quorum_error_correct_reads", "rc_gnu.py": "/usr/local/bin/rc_gnu.py", "rc_s.py": "/usr/local/bin/rc_s.py", "run_MB_SF.py": "/usr/local/bin/run_MB_SF.py", "run_MB_SF_fn.py": "/usr/local/bin/run_MB_SF_fn.py", "run_parallel_cmds.py": "/usr/local/bin/run_parallel_cmds.py", "run_quorum.py": "/usr/local/bin/run_quorum.py", "shannon.py": "/usr/local/bin/shannon.py", "split_mate_pairs": "/usr/local/bin/split_mate_pairs", "test.py": "/usr/local/bin/test.py", "test_suite.py": "/usr/local/bin/test_suite.py", "tester.py": "/usr/local/bin/tester.py", "trie.py": "/usr/local/bin/trie.py", "weight_updated_graph.py": "/usr/local/bin/weight_updated_graph.py", "jellyfish": "/usr/local/bin/jellyfish", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shannon.
shpc-registry automated BioContainers addition for shannon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shannon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shannon:0.0.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shannon/0.0.2--py_1
$ module help quay.io/biocontainers/shannon/0.0.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shannon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shannon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shannon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shannon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shannon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shannon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### algorithm_SF.py

```bash
$ singularity exec <container> /usr/local/bin/algorithm_SF.py
$ podman run --it --rm --entrypoint /usr/local/bin/algorithm_SF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/algorithm_SF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ext_corr.py

```bash
$ singularity exec <container> /usr/local/bin/ext_corr.py
$ podman run --it --rm --entrypoint /usr/local/bin/ext_corr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ext_corr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extension_correction.py

```bash
$ singularity exec <container> /usr/local/bin/extension_correction.py
$ podman run --it --rm --entrypoint /usr/local/bin/extension_correction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extension_correction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extension_correction_Kminus1.py

```bash
$ singularity exec <container> /usr/local/bin/extension_correction_Kminus1.py
$ podman run --it --rm --entrypoint /usr/local/bin/extension_correction_Kminus1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extension_correction_Kminus1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast_reps.py

```bash
$ singularity exec <container> /usr/local/bin/fast_reps.py
$ podman run --it --rm --entrypoint /usr/local/bin/fast_reps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast_reps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faster_reps.py

```bash
$ singularity exec <container> /usr/local/bin/faster_reps.py
$ podman run --it --rm --entrypoint /usr/local/bin/faster_reps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faster_reps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_FP.py

```bash
$ singularity exec <container> /usr/local/bin/filter_FP.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_FP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_FP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_FP_2s.py

```bash
$ singularity exec <container> /usr/local/bin/filter_FP_2s.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_FP_2s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_FP_2s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_kallisto.py

```bash
$ singularity exec <container> /usr/local/bin/filter_kallisto.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_kallisto.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_kallisto.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_trans.py

```bash
$ singularity exec <container> /usr/local/bin/filter_trans.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_trans.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_trans.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_reps_blat.py

```bash
$ singularity exec <container> /usr/local/bin/find_reps_blat.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_reps_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_reps_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmers_for_component.py

```bash
$ singularity exec <container> /usr/local/bin/kmers_for_component.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmers_for_component.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmers_for_component.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmers_for_component_back.py

```bash
$ singularity exec <container> /usr/local/bin/kmers_for_component_back.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmers_for_component_back.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmers_for_component_back.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kp1mer_to_kmer.py

```bash
$ singularity exec <container> /usr/local/bin/kp1mer_to_kmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/kp1mer_to_kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kp1mer_to_kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mbgraph.py

```bash
$ singularity exec <container> /usr/local/bin/mbgraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/mbgraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mbgraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/merge_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multibridging.py

```bash
$ singularity exec <container> /usr/local/bin/multibridging.py
$ podman run --it --rm --entrypoint /usr/local/bin/multibridging.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multibridging.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_blat.py

```bash
$ singularity exec <container> /usr/local/bin/parallel_blat.py
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_blat_python.py

```bash
$ singularity exec <container> /usr/local/bin/parallel_blat_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_blat_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_blat_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### path_decompose_sparse.py

```bash
$ singularity exec <container> /usr/local/bin/path_decompose_sparse.py
$ podman run --it --rm --entrypoint /usr/local/bin/path_decompose_sparse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/path_decompose_sparse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_concatenated_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/process_concatenated_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/process_concatenated_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_concatenated_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum

```bash
$ singularity exec <container> /usr/local/bin/quorum
$ podman run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_create_database

```bash
$ singularity exec <container> /usr/local/bin/quorum_create_database
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_error_correct_reads

```bash
$ singularity exec <container> /usr/local/bin/quorum_error_correct_reads
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rc_gnu.py

```bash
$ singularity exec <container> /usr/local/bin/rc_gnu.py
$ podman run --it --rm --entrypoint /usr/local/bin/rc_gnu.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rc_gnu.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rc_s.py

```bash
$ singularity exec <container> /usr/local/bin/rc_s.py
$ podman run --it --rm --entrypoint /usr/local/bin/rc_s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rc_s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_MB_SF.py

```bash
$ singularity exec <container> /usr/local/bin/run_MB_SF.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_MB_SF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_MB_SF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_MB_SF_fn.py

```bash
$ singularity exec <container> /usr/local/bin/run_MB_SF_fn.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_MB_SF_fn.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_MB_SF_fn.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_parallel_cmds.py

```bash
$ singularity exec <container> /usr/local/bin/run_parallel_cmds.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_parallel_cmds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_parallel_cmds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_quorum.py

```bash
$ singularity exec <container> /usr/local/bin/run_quorum.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_quorum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_quorum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shannon.py

```bash
$ singularity exec <container> /usr/local/bin/shannon.py
$ podman run --it --rm --entrypoint /usr/local/bin/shannon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shannon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/split_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.py

```bash
$ singularity exec <container> /usr/local/bin/test.py
$ podman run --it --rm --entrypoint /usr/local/bin/test.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_suite.py

```bash
$ singularity exec <container> /usr/local/bin/test_suite.py
$ podman run --it --rm --entrypoint /usr/local/bin/test_suite.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_suite.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tester.py

```bash
$ singularity exec <container> /usr/local/bin/tester.py
$ podman run --it --rm --entrypoint /usr/local/bin/tester.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tester.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trie.py

```bash
$ singularity exec <container> /usr/local/bin/trie.py
$ podman run --it --rm --entrypoint /usr/local/bin/trie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weight_updated_graph.py

```bash
$ singularity exec <container> /usr/local/bin/weight_updated_graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/weight_updated_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weight_updated_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)
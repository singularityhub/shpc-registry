---
layout: container
name:  "quay.io/biocontainers/medaka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/medaka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/medaka/container.yaml"
updated_at: "2024-10-15 03:33:56.194424"
latest: "2.0.0--py311hfd2b166_0"
container_url: "https://biocontainers.pro/tools/medaka"
aliases:
 - "check_compression"
 - "compress_fast5"
 - "fast5_subset"
 - "hdf2tf.py"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_haploid_variant"
 - "medaka_variant"
 - "medaka_version_report"
 - "mini_align"
 - "multi_to_single_fast5"
 - "single_to_multi_fast5"
 - "whatshap"
 - "minimap2.py"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "tar"
 - "igzip"
 - "gff2gff.py"
 - "tf_upgrade_v2"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
versions:
 - "1.2.2--py36hbcc4abb_0"
 - "1.11.3--py39h05d5c5e_0"
 - "1.10.0--py310h87e71ce_0"
 - "1.8.0--py38hdaa7744_0"
 - "1.7.2--py38h6239ad4_1"
 - "1.6.1--py38h84d2cc8_2"
 - "2.0.0--py311hfd2b166_0"
description: "shpc-registry automated BioContainers addition for medaka"
config: {"url": "https://biocontainers.pro/tools/medaka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for medaka", "latest": {"2.0.0--py311hfd2b166_0": "sha256:8d2a21ca0f28b18187f690995bc8bc58394495515b31d843613644570da8903a"}, "tags": {"1.2.2--py36hbcc4abb_0": "sha256:0962cbe886fde7a0bf162be544a0ebea035485ab759517754ea1a986c08e08d8", "1.11.3--py39h05d5c5e_0": "sha256:ac4af46fe8046c60f78f72aad077e445319d1b8b985288e9460ae5fbe846c326", "1.10.0--py310h87e71ce_0": "sha256:42f43198c4ac7429eb09d1aa9fa89ed07f0d7c0ea547c6166e50cbfba0140e47", "1.8.0--py38hdaa7744_0": "sha256:777dc707f163a3b56b5e18f066cfac3c3fc96ef029332e7c0bdd1db81ada412f", "1.7.2--py38h6239ad4_1": "sha256:0b62b4b1162d74865ddd9480c2165592e2eca51d3819afcc16b9904824251e11", "1.6.1--py38h84d2cc8_2": "sha256:6d250f5507e74b0b613ecf16949df43b609b00f0ce5b458cf4ff2890b2870c8b", "2.0.0--py311hfd2b166_0": "sha256:8d2a21ca0f28b18187f690995bc8bc58394495515b31d843613644570da8903a"}, "docker": "quay.io/biocontainers/medaka", "aliases": {"check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "fast5_subset": "/usr/local/bin/fast5_subset", "hdf2tf.py": "/usr/local/bin/hdf2tf.py", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_haploid_variant": "/usr/local/bin/medaka_haploid_variant", "medaka_variant": "/usr/local/bin/medaka_variant", "medaka_version_report": "/usr/local/bin/medaka_version_report", "mini_align": "/usr/local/bin/mini_align", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "whatshap": "/usr/local/bin/whatshap", "minimap2.py": "/usr/local/bin/minimap2.py", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "tar": "/usr/local/bin/tar", "igzip": "/usr/local/bin/igzip", "gff2gff.py": "/usr/local/bin/gff2gff.py", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/medaka.
shpc-registry automated BioContainers addition for medaka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/medaka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/medaka:2.0.0--py311hfd2b166_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/medaka/2.0.0--py311hfd2b166_0
$ module help quay.io/biocontainers/medaka/2.0.0--py311hfd2b166_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### medaka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### medaka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### medaka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### medaka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### medaka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### medaka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_compression

```bash
$ singularity exec <container> /usr/local/bin/check_compression
$ podman run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_fast5

```bash
$ singularity exec <container> /usr/local/bin/compress_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5_subset

```bash
$ singularity exec <container> /usr/local/bin/fast5_subset
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2tf.py

```bash
$ singularity exec <container> /usr/local/bin/hdf2tf.py
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka

```bash
$ singularity exec <container> /usr/local/bin/medaka
$ podman run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_counts

```bash
$ singularity exec <container> /usr/local/bin/medaka_counts
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_data_path

```bash
$ singularity exec <container> /usr/local/bin/medaka_data_path
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_haploid_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_haploid_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_version_report

```bash
$ singularity exec <container> /usr/local/bin/medaka_version_report
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
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
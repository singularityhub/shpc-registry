---
layout: container
name:  "quay.io/biocontainers/bayesase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bayesase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bayesase/container.yaml"
updated_at: "2023-10-12 03:13:54.437996"
latest: "21.1.13.1--py_0"
container_url: "https://biocontainers.pro/tools/bayesase"
aliases:
 - "bwa_split_sam_seonly_2output.py"
 - "calculate_priors_ase_count_tables.py"
 - "check_aln_design_file.py"
 - "check_comparate_design_file.py"
 - "check_lost_reads.py"
 - "check_sam_present.py"
 - "check_samcomp_lost_reads.py"
 - "combine_count_tables.py"
 - "merge_comparates_generate_bayesian_headers.py"
 - "merge_priors_to_comparate.py"
 - "nbmodel_stan2.py"
 - "sam_compare_w_feature.py"
 - "summarize_sam_compare_cnts_table_1cond.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "c89"
 - "c99"
versions:
 - "21.1.7--py_0"
 - "21.1.13.1--py_0"
description: "shpc-registry automated BioContainers addition for bayesase"
config: {"url": "https://biocontainers.pro/tools/bayesase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bayesase", "latest": {"21.1.13.1--py_0": "sha256:65df19876dde65855d99dc18ddd6897d84b400041ab3dfc8f50349c5d4c82c8e"}, "tags": {"21.1.7--py_0": "sha256:bc9b6df00e9c590ac362268a7482da4cb8e93134faebfe9ab97b7c342be3d1a8", "21.1.13.1--py_0": "sha256:65df19876dde65855d99dc18ddd6897d84b400041ab3dfc8f50349c5d4c82c8e"}, "docker": "quay.io/biocontainers/bayesase", "aliases": {"bwa_split_sam_seonly_2output.py": "/usr/local/bin/bwa_split_sam_seonly_2output.py", "calculate_priors_ase_count_tables.py": "/usr/local/bin/calculate_priors_ase_count_tables.py", "check_aln_design_file.py": "/usr/local/bin/check_aln_design_file.py", "check_comparate_design_file.py": "/usr/local/bin/check_comparate_design_file.py", "check_lost_reads.py": "/usr/local/bin/check_lost_reads.py", "check_sam_present.py": "/usr/local/bin/check_sam_present.py", "check_samcomp_lost_reads.py": "/usr/local/bin/check_samcomp_lost_reads.py", "combine_count_tables.py": "/usr/local/bin/combine_count_tables.py", "merge_comparates_generate_bayesian_headers.py": "/usr/local/bin/merge_comparates_generate_bayesian_headers.py", "merge_priors_to_comparate.py": "/usr/local/bin/merge_priors_to_comparate.py", "nbmodel_stan2.py": "/usr/local/bin/nbmodel_stan2.py", "sam_compare_w_feature.py": "/usr/local/bin/sam_compare_w_feature.py", "summarize_sam_compare_cnts_table_1cond.py": "/usr/local/bin/summarize_sam_compare_cnts_table_1cond.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bayesase.
shpc-registry automated BioContainers addition for bayesase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bayesase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bayesase:21.1.13.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bayesase/21.1.13.1--py_0
$ module help quay.io/biocontainers/bayesase/21.1.13.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bayesase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bayesase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bayesase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bayesase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bayesase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bayesase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa_split_sam_seonly_2output.py

```bash
$ singularity exec <container> /usr/local/bin/bwa_split_sam_seonly_2output.py
$ podman run --it --rm --entrypoint /usr/local/bin/bwa_split_sam_seonly_2output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa_split_sam_seonly_2output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_priors_ase_count_tables.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_priors_ase_count_tables.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_priors_ase_count_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_priors_ase_count_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_aln_design_file.py

```bash
$ singularity exec <container> /usr/local/bin/check_aln_design_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_aln_design_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_aln_design_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_comparate_design_file.py

```bash
$ singularity exec <container> /usr/local/bin/check_comparate_design_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_comparate_design_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_comparate_design_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_lost_reads.py

```bash
$ singularity exec <container> /usr/local/bin/check_lost_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_lost_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_lost_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_sam_present.py

```bash
$ singularity exec <container> /usr/local/bin/check_sam_present.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_sam_present.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_sam_present.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_samcomp_lost_reads.py

```bash
$ singularity exec <container> /usr/local/bin/check_samcomp_lost_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_samcomp_lost_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_samcomp_lost_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_count_tables.py

```bash
$ singularity exec <container> /usr/local/bin/combine_count_tables.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_count_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_count_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_comparates_generate_bayesian_headers.py

```bash
$ singularity exec <container> /usr/local/bin/merge_comparates_generate_bayesian_headers.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_comparates_generate_bayesian_headers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_comparates_generate_bayesian_headers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_priors_to_comparate.py

```bash
$ singularity exec <container> /usr/local/bin/merge_priors_to_comparate.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_priors_to_comparate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_priors_to_comparate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nbmodel_stan2.py

```bash
$ singularity exec <container> /usr/local/bin/nbmodel_stan2.py
$ podman run --it --rm --entrypoint /usr/local/bin/nbmodel_stan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nbmodel_stan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_compare_w_feature.py

```bash
$ singularity exec <container> /usr/local/bin/sam_compare_w_feature.py
$ podman run --it --rm --entrypoint /usr/local/bin/sam_compare_w_feature.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_compare_w_feature.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize_sam_compare_cnts_table_1cond.py

```bash
$ singularity exec <container> /usr/local/bin/summarize_sam_compare_cnts_table_1cond.py
$ podman run --it --rm --entrypoint /usr/local/bin/summarize_sam_compare_cnts_table_1cond.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize_sam_compare_cnts_table_1cond.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/run-dbcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/run-dbcan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/run-dbcan/container.yaml"
updated_at: "2023-10-18 03:09:24.957178"
latest: "2.0.11--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/run-dbcan"
aliases:
 - "CGCFinder.py"
 - "FragGeneScan"
 - "add_functions_orf.py"
 - "bact_group_many_proteins_many_patterns.py"
 - "hmmscan-parser.py"
 - "list_multidomain_proteins.py"
 - "parallel_group_many_proteins_many_patterns_noDNA.py"
 - "run_FragGeneScan.pl"
 - "run_dbcan.py"
 - "train_many_organisms_many_families.py"
 - "diamond"
 - "perl5.32.0"
 - "natsort"
 - "prodigal"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
versions:
 - "2.0.11--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for run-dbcan"
config: {"url": "https://biocontainers.pro/tools/run-dbcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for run-dbcan", "latest": {"2.0.11--pyh3252c3a_0": "sha256:3e76d779763739eb5804a5cf22e761635bbc4ab3ae7d6228150125be2e352341"}, "tags": {"2.0.11--pyh3252c3a_0": "sha256:3e76d779763739eb5804a5cf22e761635bbc4ab3ae7d6228150125be2e352341"}, "docker": "quay.io/biocontainers/run-dbcan", "aliases": {"CGCFinder.py": "/usr/local/bin/CGCFinder.py", "FragGeneScan": "/usr/local/bin/FragGeneScan", "add_functions_orf.py": "/usr/local/bin/add_functions_orf.py", "bact_group_many_proteins_many_patterns.py": "/usr/local/bin/bact_group_many_proteins_many_patterns.py", "hmmscan-parser.py": "/usr/local/bin/hmmscan-parser.py", "list_multidomain_proteins.py": "/usr/local/bin/list_multidomain_proteins.py", "parallel_group_many_proteins_many_patterns_noDNA.py": "/usr/local/bin/parallel_group_many_proteins_many_patterns_noDNA.py", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "run_dbcan.py": "/usr/local/bin/run_dbcan.py", "train_many_organisms_many_families.py": "/usr/local/bin/train_many_organisms_many_families.py", "diamond": "/usr/local/bin/diamond", "perl5.32.0": "/usr/local/bin/perl5.32.0", "natsort": "/usr/local/bin/natsort", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/run-dbcan.
shpc-registry automated BioContainers addition for run-dbcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/run-dbcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/run-dbcan:2.0.11--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/run-dbcan/2.0.11--pyh3252c3a_0
$ module help quay.io/biocontainers/run-dbcan/2.0.11--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### run-dbcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### run-dbcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### run-dbcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### run-dbcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### run-dbcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### run-dbcan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CGCFinder.py

```bash
$ singularity exec <container> /usr/local/bin/CGCFinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/CGCFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CGCFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_functions_orf.py

```bash
$ singularity exec <container> /usr/local/bin/add_functions_orf.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_functions_orf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_functions_orf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bact_group_many_proteins_many_patterns.py

```bash
$ singularity exec <container> /usr/local/bin/bact_group_many_proteins_many_patterns.py
$ podman run --it --rm --entrypoint /usr/local/bin/bact_group_many_proteins_many_patterns.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bact_group_many_proteins_many_patterns.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmscan-parser.py

```bash
$ singularity exec <container> /usr/local/bin/hmmscan-parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmmscan-parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmscan-parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list_multidomain_proteins.py

```bash
$ singularity exec <container> /usr/local/bin/list_multidomain_proteins.py
$ podman run --it --rm --entrypoint /usr/local/bin/list_multidomain_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list_multidomain_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_group_many_proteins_many_patterns_noDNA.py

```bash
$ singularity exec <container> /usr/local/bin/parallel_group_many_proteins_many_patterns_noDNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_group_many_proteins_many_patterns_noDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_group_many_proteins_many_patterns_noDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_dbcan.py

```bash
$ singularity exec <container> /usr/local/bin/run_dbcan.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_dbcan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_dbcan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_many_organisms_many_families.py

```bash
$ singularity exec <container> /usr/local/bin/train_many_organisms_many_families.py
$ podman run --it --rm --entrypoint /usr/local/bin/train_many_organisms_many_families.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_many_organisms_many_families.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
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
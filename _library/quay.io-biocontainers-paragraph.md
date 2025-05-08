---
layout: container
name:  "quay.io/biocontainers/paragraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paragraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paragraph/container.yaml"
updated_at: "2025-05-08 05:32:09.261692"
latest: "2.3--h21f15d8_1"
container_url: "https://biocontainers.pro/tools/paragraph"
aliases:
 - "__init__.py"
 - "addVariants.py"
 - "compare-alignments.py"
 - "findgrm.py"
 - "graph-to-fasta"
 - "grmpy"
 - "grmpy-vcf-merge.py"
 - "idxdepth"
 - "kmerstats"
 - "msa2vcf.py"
 - "multigrmpy.py"
 - "multiparagraph.py"
 - "pam"
 - "paragraph"
 - "paragraph2dot.py"
 - "test_blackbox"
 - "test_grm"
 - "vcf2paragraph.py"
 - "jsonschema"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "htsfile"
versions:
 - "2.3--h21f15d8_1"
description: "shpc-registry automated BioContainers addition for paragraph"
config: {"url": "https://biocontainers.pro/tools/paragraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for paragraph", "latest": {"2.3--h21f15d8_1": "sha256:1ef204d04d1ca59bef259497854add78e14aa98994e6ed26fc3b241fe906eb1a"}, "tags": {"2.3--h21f15d8_1": "sha256:1ef204d04d1ca59bef259497854add78e14aa98994e6ed26fc3b241fe906eb1a"}, "docker": "quay.io/biocontainers/paragraph", "aliases": {"__init__.py": "/usr/local/bin/__init__.py", "addVariants.py": "/usr/local/bin/addVariants.py", "compare-alignments.py": "/usr/local/bin/compare-alignments.py", "findgrm.py": "/usr/local/bin/findgrm.py", "graph-to-fasta": "/usr/local/bin/graph-to-fasta", "grmpy": "/usr/local/bin/grmpy", "grmpy-vcf-merge.py": "/usr/local/bin/grmpy-vcf-merge.py", "idxdepth": "/usr/local/bin/idxdepth", "kmerstats": "/usr/local/bin/kmerstats", "msa2vcf.py": "/usr/local/bin/msa2vcf.py", "multigrmpy.py": "/usr/local/bin/multigrmpy.py", "multiparagraph.py": "/usr/local/bin/multiparagraph.py", "pam": "/usr/local/bin/pam", "paragraph": "/usr/local/bin/paragraph", "paragraph2dot.py": "/usr/local/bin/paragraph2dot.py", "test_blackbox": "/usr/local/bin/test_blackbox", "test_grm": "/usr/local/bin/test_grm", "vcf2paragraph.py": "/usr/local/bin/vcf2paragraph.py", "jsonschema": "/usr/local/bin/jsonschema", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "htsfile": "/usr/local/bin/htsfile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paragraph.
shpc-registry automated BioContainers addition for paragraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paragraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paragraph:2.3--h21f15d8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paragraph/2.3--h21f15d8_1
$ module help quay.io/biocontainers/paragraph/2.3--h21f15d8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paragraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paragraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paragraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paragraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paragraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paragraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### __init__.py

```bash
$ singularity exec <container> /usr/local/bin/__init__.py
$ podman run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addVariants.py

```bash
$ singularity exec <container> /usr/local/bin/addVariants.py
$ podman run --it --rm --entrypoint /usr/local/bin/addVariants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addVariants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-alignments.py

```bash
$ singularity exec <container> /usr/local/bin/compare-alignments.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare-alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findgrm.py

```bash
$ singularity exec <container> /usr/local/bin/findgrm.py
$ podman run --it --rm --entrypoint /usr/local/bin/findgrm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findgrm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/graph-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/graph-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grmpy

```bash
$ singularity exec <container> /usr/local/bin/grmpy
$ podman run --it --rm --entrypoint /usr/local/bin/grmpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grmpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grmpy-vcf-merge.py

```bash
$ singularity exec <container> /usr/local/bin/grmpy-vcf-merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/grmpy-vcf-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grmpy-vcf-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idxdepth

```bash
$ singularity exec <container> /usr/local/bin/idxdepth
$ podman run --it --rm --entrypoint /usr/local/bin/idxdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idxdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerstats

```bash
$ singularity exec <container> /usr/local/bin/kmerstats
$ podman run --it --rm --entrypoint /usr/local/bin/kmerstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa2vcf.py

```bash
$ singularity exec <container> /usr/local/bin/msa2vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/msa2vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa2vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multigrmpy.py

```bash
$ singularity exec <container> /usr/local/bin/multigrmpy.py
$ podman run --it --rm --entrypoint /usr/local/bin/multigrmpy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multigrmpy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiparagraph.py

```bash
$ singularity exec <container> /usr/local/bin/multiparagraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/multiparagraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiparagraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pam

```bash
$ singularity exec <container> /usr/local/bin/pam
$ podman run --it --rm --entrypoint /usr/local/bin/pam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paragraph

```bash
$ singularity exec <container> /usr/local/bin/paragraph
$ podman run --it --rm --entrypoint /usr/local/bin/paragraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paragraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paragraph2dot.py

```bash
$ singularity exec <container> /usr/local/bin/paragraph2dot.py
$ podman run --it --rm --entrypoint /usr/local/bin/paragraph2dot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paragraph2dot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_blackbox

```bash
$ singularity exec <container> /usr/local/bin/test_blackbox
$ podman run --it --rm --entrypoint /usr/local/bin/test_blackbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_blackbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_grm

```bash
$ singularity exec <container> /usr/local/bin/test_grm
$ podman run --it --rm --entrypoint /usr/local/bin/test_grm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_grm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2paragraph.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2paragraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2paragraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2paragraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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
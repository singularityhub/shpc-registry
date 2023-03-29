---
layout: container
name:  "quay.io/biocontainers/forgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/forgi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/forgi/container.yaml"
updated_at: "2023-03-29 03:17:59.261933"
latest: "2.1.1--py36hffcf100_1"
container_url: "https://biocontainers.pro/tools/forgi"
aliases:
 - "compare_RNA.py"
 - "describe_cg.py"
 - "forgi_config.py"
 - "pseudoknot_analyzer.py"
 - "rnaConvert.py"
 - "visualize_rna.py"
 - "f2py3.6"
 - "futurize"
 - "pasteurize"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
versions:
 - "2.1.1--py36hffcf100_1"
description: "shpc-registry automated BioContainers addition for forgi"
config: {"url": "https://biocontainers.pro/tools/forgi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for forgi", "latest": {"2.1.1--py36hffcf100_1": "sha256:240b3bc7b02fdc9b3961d97633e5e325c8247dbef6a5846ef33efdcc2b83255d"}, "tags": {"2.1.1--py36hffcf100_1": "sha256:240b3bc7b02fdc9b3961d97633e5e325c8247dbef6a5846ef33efdcc2b83255d"}, "docker": "quay.io/biocontainers/forgi", "aliases": {"compare_RNA.py": "/usr/local/bin/compare_RNA.py", "describe_cg.py": "/usr/local/bin/describe_cg.py", "forgi_config.py": "/usr/local/bin/forgi_config.py", "pseudoknot_analyzer.py": "/usr/local/bin/pseudoknot_analyzer.py", "rnaConvert.py": "/usr/local/bin/rnaConvert.py", "visualize_rna.py": "/usr/local/bin/visualize_rna.py", "f2py3.6": "/usr/local/bin/f2py3.6", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/forgi.
shpc-registry automated BioContainers addition for forgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/forgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/forgi:2.1.1--py36hffcf100_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/forgi/2.1.1--py36hffcf100_1
$ module help quay.io/biocontainers/forgi/2.1.1--py36hffcf100_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### forgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### forgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### forgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### forgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### forgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### forgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_RNA.py

```bash
$ singularity exec <container> /usr/local/bin/compare_RNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_RNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_RNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### describe_cg.py

```bash
$ singularity exec <container> /usr/local/bin/describe_cg.py
$ podman run --it --rm --entrypoint /usr/local/bin/describe_cg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/describe_cg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### forgi_config.py

```bash
$ singularity exec <container> /usr/local/bin/forgi_config.py
$ podman run --it --rm --entrypoint /usr/local/bin/forgi_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/forgi_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pseudoknot_analyzer.py

```bash
$ singularity exec <container> /usr/local/bin/pseudoknot_analyzer.py
$ podman run --it --rm --entrypoint /usr/local/bin/pseudoknot_analyzer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pseudoknot_analyzer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaConvert.py

```bash
$ singularity exec <container> /usr/local/bin/rnaConvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaConvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaConvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize_rna.py

```bash
$ singularity exec <container> /usr/local/bin/visualize_rna.py
$ podman run --it --rm --entrypoint /usr/local/bin/visualize_rna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize_rna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
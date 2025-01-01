---
layout: container
name:  "quay.io/biocontainers/tsebra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tsebra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tsebra/container.yaml"
updated_at: "2025-01-01 03:09:25.084781"
latest: "1.1.2.5--pyhca03a8a_0"
container_url: "https://biocontainers.pro/tools/tsebra"
aliases:
 - "evidence.py"
 - "features.py"
 - "fix_gtf_ids.py"
 - "genome_anno.py"
 - "get_longest_isoform.py"
 - "overlap_graph.py"
 - "rename_gtf.py"
 - "tsebra.py"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "1.1.1--pyhca03a8a_0"
 - "1.1.2--pyhca03a8a_0"
 - "1.1.2.2--pyhca03a8a_0"
 - "1.1.2.4--pyhca03a8a_0"
 - "1.1.2.5--pyhca03a8a_0"
description: "singularity registry hpc automated addition for tsebra"
config: {"url": "https://biocontainers.pro/tools/tsebra", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tsebra", "latest": {"1.1.2.5--pyhca03a8a_0": "sha256:123dad62998b9cc2fb2b0d7590eeed4b678b6e41ce05c8a50b271a55922e52ef"}, "tags": {"1.1.1--pyhca03a8a_0": "sha256:9203773dc6c39f1448b1eddd9ab33cb5b05409ba84fb939e110f89f21e464fdf", "1.1.2--pyhca03a8a_0": "sha256:cf1d149ccbe505772a95fb61ac39fe41a59ac23968d7aaa9ab67054161fa9102", "1.1.2.2--pyhca03a8a_0": "sha256:eb2c66ec0e47a8d56b20ec6a6fe713ba1f47e5bf0ce6ef035122f893616a2282", "1.1.2.4--pyhca03a8a_0": "sha256:211158a8c75e560bf2e7a4f899b988c12634768eabfe8707c0f6bd9adc547f43", "1.1.2.5--pyhca03a8a_0": "sha256:123dad62998b9cc2fb2b0d7590eeed4b678b6e41ce05c8a50b271a55922e52ef"}, "docker": "quay.io/biocontainers/tsebra", "aliases": {"evidence.py": "/usr/local/bin/evidence.py", "features.py": "/usr/local/bin/features.py", "fix_gtf_ids.py": "/usr/local/bin/fix_gtf_ids.py", "genome_anno.py": "/usr/local/bin/genome_anno.py", "get_longest_isoform.py": "/usr/local/bin/get_longest_isoform.py", "overlap_graph.py": "/usr/local/bin/overlap_graph.py", "rename_gtf.py": "/usr/local/bin/rename_gtf.py", "tsebra.py": "/usr/local/bin/tsebra.py", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tsebra.
singularity registry hpc automated addition for tsebra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tsebra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tsebra:1.1.2.5--pyhca03a8a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tsebra/1.1.2.5--pyhca03a8a_0
$ module help quay.io/biocontainers/tsebra/1.1.2.5--pyhca03a8a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tsebra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tsebra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tsebra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tsebra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tsebra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tsebra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### evidence.py

```bash
$ singularity exec <container> /usr/local/bin/evidence.py
$ podman run --it --rm --entrypoint /usr/local/bin/evidence.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evidence.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### features.py

```bash
$ singularity exec <container> /usr/local/bin/features.py
$ podman run --it --rm --entrypoint /usr/local/bin/features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_gtf_ids.py

```bash
$ singularity exec <container> /usr/local/bin/fix_gtf_ids.py
$ podman run --it --rm --entrypoint /usr/local/bin/fix_gtf_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_gtf_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_anno.py

```bash
$ singularity exec <container> /usr/local/bin/genome_anno.py
$ podman run --it --rm --entrypoint /usr/local/bin/genome_anno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_anno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_longest_isoform.py

```bash
$ singularity exec <container> /usr/local/bin/get_longest_isoform.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_longest_isoform.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_longest_isoform.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### overlap_graph.py

```bash
$ singularity exec <container> /usr/local/bin/overlap_graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/overlap_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/overlap_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_gtf.py

```bash
$ singularity exec <container> /usr/local/bin/rename_gtf.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsebra.py

```bash
$ singularity exec <container> /usr/local/bin/tsebra.py
$ podman run --it --rm --entrypoint /usr/local/bin/tsebra.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsebra.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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
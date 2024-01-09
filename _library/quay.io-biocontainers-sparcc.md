---
layout: container
name:  "quay.io/biocontainers/sparcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sparcc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sparcc/container.yaml"
updated_at: "2024-01-09 02:46:33.989694"
latest: "0.1.0--0"
container_url: "https://biocontainers.pro/tools/sparcc"
aliases:
 - "Lineages.py"
 - "MakeBootstraps.py"
 - "PseudoPvals.py"
 - "SampleDist.py"
 - "SparCC.py"
 - "__init__.py"
 - "analysis_methods.py"
 - "compositional_methods.py"
 - "core_methods.py"
 - "io_methods.py"
 - "conv-template"
 - "from-template"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.1.0--0"
description: "shpc-registry automated BioContainers addition for sparcc"
config: {"url": "https://biocontainers.pro/tools/sparcc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sparcc", "latest": {"0.1.0--0": "sha256:903a25a57b8360a0293601350420c8f13fcb043eacf5b3ecc7d9d25a9be05804"}, "tags": {"0.1.0--0": "sha256:903a25a57b8360a0293601350420c8f13fcb043eacf5b3ecc7d9d25a9be05804"}, "docker": "quay.io/biocontainers/sparcc", "aliases": {"Lineages.py": "/usr/local/bin/Lineages.py", "MakeBootstraps.py": "/usr/local/bin/MakeBootstraps.py", "PseudoPvals.py": "/usr/local/bin/PseudoPvals.py", "SampleDist.py": "/usr/local/bin/SampleDist.py", "SparCC.py": "/usr/local/bin/SparCC.py", "__init__.py": "/usr/local/bin/__init__.py", "analysis_methods.py": "/usr/local/bin/analysis_methods.py", "compositional_methods.py": "/usr/local/bin/compositional_methods.py", "core_methods.py": "/usr/local/bin/core_methods.py", "io_methods.py": "/usr/local/bin/io_methods.py", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sparcc.
shpc-registry automated BioContainers addition for sparcc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sparcc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sparcc:0.1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sparcc/0.1.0--0
$ module help quay.io/biocontainers/sparcc/0.1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sparcc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sparcc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sparcc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sparcc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sparcc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sparcc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Lineages.py

```bash
$ singularity exec <container> /usr/local/bin/Lineages.py
$ podman run --it --rm --entrypoint /usr/local/bin/Lineages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Lineages.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeBootstraps.py

```bash
$ singularity exec <container> /usr/local/bin/MakeBootstraps.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeBootstraps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeBootstraps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PseudoPvals.py

```bash
$ singularity exec <container> /usr/local/bin/PseudoPvals.py
$ podman run --it --rm --entrypoint /usr/local/bin/PseudoPvals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PseudoPvals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SampleDist.py

```bash
$ singularity exec <container> /usr/local/bin/SampleDist.py
$ podman run --it --rm --entrypoint /usr/local/bin/SampleDist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SampleDist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SparCC.py

```bash
$ singularity exec <container> /usr/local/bin/SparCC.py
$ podman run --it --rm --entrypoint /usr/local/bin/SparCC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SparCC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### __init__.py

```bash
$ singularity exec <container> /usr/local/bin/__init__.py
$ podman run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analysis_methods.py

```bash
$ singularity exec <container> /usr/local/bin/analysis_methods.py
$ podman run --it --rm --entrypoint /usr/local/bin/analysis_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analysis_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compositional_methods.py

```bash
$ singularity exec <container> /usr/local/bin/compositional_methods.py
$ podman run --it --rm --entrypoint /usr/local/bin/compositional_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compositional_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### core_methods.py

```bash
$ singularity exec <container> /usr/local/bin/core_methods.py
$ podman run --it --rm --entrypoint /usr/local/bin/core_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/core_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_methods.py

```bash
$ singularity exec <container> /usr/local/bin/io_methods.py
$ podman run --it --rm --entrypoint /usr/local/bin/io_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_methods.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
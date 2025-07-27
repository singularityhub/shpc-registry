---
layout: container
name:  "quay.io/biocontainers/drop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/drop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/drop/container.yaml"
updated_at: "2025-07-27 04:24:39.805115"
latest: "1.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/drop"
aliases:
 - "drop"
 - "git2_cli"
 - "wbuild"
 - "gatk"
 - "STAR"
 - "STARlong"
 - "plac_runner.py"
 - "yte"
 - "bc"
 - "dc"
 - "docutils"
 - "pulptest"
 - "gff2gff.py"
versions:
 - "1.2.2--pyhdfd78af_0"
 - "1.2.4--pyhdfd78af_0"
 - "1.3.3--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
 - "1.3.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for drop"
config: {"url": "https://biocontainers.pro/tools/drop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for drop", "latest": {"1.4.0--pyhdfd78af_0": "sha256:9adc4a1589468cb6cbf36504557749bb556ca44f3048b257e203ba9e341149fb"}, "tags": {"1.2.2--pyhdfd78af_0": "sha256:4f844567e238de0bb3d2e5f90f921386b6db893371ae2b481fa43cbc0df2153e", "1.2.4--pyhdfd78af_0": "sha256:a674737190f379c27cb4604103c15f87696686a5882a7d6de1ee827b67e11a74", "1.3.3--pyhdfd78af_0": "sha256:cbf3da1b2ae8698b1c366970354245e7647b0d3512404b7739527ee0a7b83a82", "1.4.0--pyhdfd78af_0": "sha256:9adc4a1589468cb6cbf36504557749bb556ca44f3048b257e203ba9e341149fb", "1.3.4--pyhdfd78af_0": "sha256:c22baed8c4bac345b912cbb653a442dea18aafe13ceb37e56739014e1c24100a"}, "docker": "quay.io/biocontainers/drop", "aliases": {"drop": "/usr/local/bin/drop", "git2_cli": "/usr/local/bin/git2_cli", "wbuild": "/usr/local/bin/wbuild", "gatk": "/usr/local/bin/gatk", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "docutils": "/usr/local/bin/docutils", "pulptest": "/usr/local/bin/pulptest", "gff2gff.py": "/usr/local/bin/gff2gff.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/drop.
shpc-registry automated BioContainers addition for drop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/drop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/drop:1.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/drop/1.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/drop/1.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### drop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### drop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### drop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### drop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### drop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### drop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### drop

```bash
$ singularity exec <container> /usr/local/bin/drop
$ podman run --it --rm --entrypoint /usr/local/bin/drop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2_cli

```bash
$ singularity exec <container> /usr/local/bin/git2_cli
$ podman run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wbuild

```bash
$ singularity exec <container> /usr/local/bin/wbuild
$ podman run --it --rm --entrypoint /usr/local/bin/wbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk

```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/staphopia-sccmec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphopia-sccmec/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/staphopia-sccmec/container.yaml"
updated_at: "2022-10-29 05:38:50.073710"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/staphopia-sccmec"
aliases:
 - "executor"
 - "staphopia-sccmec"
 - "2to3-3.9"
 - "CA.pm"
 - "accn-at-a-time"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asp-cp"
 - "asp-ls"
 - "between-two-genes"
 - "blast_formatter"
 - "blastdb_aliastool"
versions:
 - "1.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for staphopia-sccmec"
config: {"url": "https://biocontainers.pro/tools/staphopia-sccmec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for staphopia-sccmec", "latest": {"1.0.0--hdfd78af_0": "sha256:f006276565254f788bee4adc73d146959ade537ecd7b14501a725401fd1dea87"}, "tags": {"1.0.0--hdfd78af_0": "sha256:f006276565254f788bee4adc73d146959ade537ecd7b14501a725401fd1dea87"}, "docker": "quay.io/biocontainers/staphopia-sccmec", "aliases": {"executor": "/usr/local/bin/executor", "staphopia-sccmec": "/usr/local/bin/staphopia-sccmec", "2to3-3.9": "/usr/local/bin/2to3-3.9", "CA.pm": "/usr/local/bin/CA.pm", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "between-two-genes": "/usr/local/bin/between-two-genes", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphopia-sccmec.
shpc-registry automated BioContainers addition for staphopia-sccmec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphopia-sccmec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphopia-sccmec:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphopia-sccmec/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/staphopia-sccmec/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphopia-sccmec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphopia-sccmec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphopia-sccmec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphopia-sccmec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphopia-sccmec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphopia-sccmec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### staphopia-sccmec

```bash
$ singularity exec <container> /usr/local/bin/staphopia-sccmec
$ podman run --it --rm --entrypoint /usr/local/bin/staphopia-sccmec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/staphopia-sccmec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
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
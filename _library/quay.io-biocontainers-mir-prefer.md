---
layout: container
name:  "quay.io/biocontainers/mir-prefer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mir-prefer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mir-prefer/container.yaml"
updated_at: "2022-10-27 01:10:40.945661"
latest: "0.24--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/mir-prefer"
aliases:
 - "bowtie-align-reads.py"
 - "convert-mirdeep2-fasta.py"
 - "convert-readcount-file.py"
 - "miR_PREFeR.py"
 - "process-reads-fasta.py"
versions:
 - "0.24--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for mir-prefer"
config: {"url": "https://biocontainers.pro/tools/mir-prefer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mir-prefer", "latest": {"0.24--hdfd78af_4": "sha256:2ae66576ec3e8cca0317394ffab369617a943e5f0970e0877e31dd3d6e3da211"}, "tags": {"0.24--hdfd78af_4": "sha256:2ae66576ec3e8cca0317394ffab369617a943e5f0970e0877e31dd3d6e3da211"}, "docker": "quay.io/biocontainers/mir-prefer", "aliases": {"bowtie-align-reads.py": "/usr/local/bin/bowtie-align-reads.py", "convert-mirdeep2-fasta.py": "/usr/local/bin/convert-mirdeep2-fasta.py", "convert-readcount-file.py": "/usr/local/bin/convert-readcount-file.py", "miR_PREFeR.py": "/usr/local/bin/miR_PREFeR.py", "process-reads-fasta.py": "/usr/local/bin/process-reads-fasta.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mir-prefer.
shpc-registry automated BioContainers addition for mir-prefer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mir-prefer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mir-prefer:0.24--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mir-prefer/0.24--hdfd78af_4
$ module help quay.io/biocontainers/mir-prefer/0.24--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mir-prefer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mir-prefer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mir-prefer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mir-prefer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mir-prefer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mir-prefer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bowtie-align-reads.py

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-mirdeep2-fasta.py

```bash
$ singularity exec <container> /usr/local/bin/convert-mirdeep2-fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert-mirdeep2-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-mirdeep2-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-readcount-file.py

```bash
$ singularity exec <container> /usr/local/bin/convert-readcount-file.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert-readcount-file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-readcount-file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miR_PREFeR.py

```bash
$ singularity exec <container> /usr/local/bin/miR_PREFeR.py
$ podman run --it --rm --entrypoint /usr/local/bin/miR_PREFeR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miR_PREFeR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process-reads-fasta.py

```bash
$ singularity exec <container> /usr/local/bin/process-reads-fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/process-reads-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process-reads-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
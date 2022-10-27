---
layout: container
name:  "quay.io/biocontainers/saspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/saspector/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/saspector/container.yaml"
updated_at: "2022-10-27 01:03:41.793546"
latest: "0.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/saspector"
aliases:
 - "SASpector"
 - "coverage.py"
 - "gene_predict.py"
 - "kmer.py"
 - "mapper.py"
 - "quastunmap.py"
 - "select_mash.py"
 - "sourmash"
 - "summary.py"
 - "tandem_repeats.py"
versions:
 - "0.0.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for saspector"
config: {"url": "https://biocontainers.pro/tools/saspector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for saspector", "latest": {"0.0.5--pyhdfd78af_0": "sha256:f31f4140479e99f4719863cd8bddfd4fd0c6c12ffa8d38a92e52d29943833f56"}, "tags": {"0.0.5--pyhdfd78af_0": "sha256:f31f4140479e99f4719863cd8bddfd4fd0c6c12ffa8d38a92e52d29943833f56"}, "docker": "quay.io/biocontainers/saspector", "aliases": {"SASpector": "/usr/local/bin/SASpector", "coverage.py": "/usr/local/bin/coverage.py", "gene_predict.py": "/usr/local/bin/gene_predict.py", "kmer.py": "/usr/local/bin/kmer.py", "mapper.py": "/usr/local/bin/mapper.py", "quastunmap.py": "/usr/local/bin/quastunmap.py", "select_mash.py": "/usr/local/bin/select_mash.py", "sourmash": "/usr/local/bin/sourmash", "summary.py": "/usr/local/bin/summary.py", "tandem_repeats.py": "/usr/local/bin/tandem_repeats.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/saspector.
shpc-registry automated BioContainers addition for saspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/saspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/saspector:0.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/saspector/0.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/saspector/0.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### saspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### saspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### saspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### saspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### saspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### saspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SASpector

```bash
$ singularity exec <container> /usr/local/bin/SASpector
$ podman run --it --rm --entrypoint /usr/local/bin/SASpector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SASpector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage.py

```bash
$ singularity exec <container> /usr/local/bin/coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_predict.py

```bash
$ singularity exec <container> /usr/local/bin/gene_predict.py
$ podman run --it --rm --entrypoint /usr/local/bin/gene_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer.py

```bash
$ singularity exec <container> /usr/local/bin/kmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapper.py

```bash
$ singularity exec <container> /usr/local/bin/mapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quastunmap.py

```bash
$ singularity exec <container> /usr/local/bin/quastunmap.py
$ podman run --it --rm --entrypoint /usr/local/bin/quastunmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quastunmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_mash.py

```bash
$ singularity exec <container> /usr/local/bin/select_mash.py
$ podman run --it --rm --entrypoint /usr/local/bin/select_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary.py

```bash
$ singularity exec <container> /usr/local/bin/summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tandem_repeats.py

```bash
$ singularity exec <container> /usr/local/bin/tandem_repeats.py
$ podman run --it --rm --entrypoint /usr/local/bin/tandem_repeats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem_repeats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
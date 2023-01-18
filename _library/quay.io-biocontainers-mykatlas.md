---
layout: container
name:  "quay.io/biocontainers/mykatlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mykatlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mykatlas/container.yaml"
updated_at: "2023-01-18 03:10:17.800157"
latest: "0.6.1--py27h21c881e_5"
container_url: "https://biocontainers.pro/tools/mykatlas"
aliases:
 - "atlas"
 - "mccortex31"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "f2py2"
 - "f2py2.7"
 - "futurize"
 - "pasteurize"
 - "python2-config"
 - "python2.7-config"
 - "python2"
versions:
 - "0.6.1--py27h21c881e_5"
description: "shpc-registry automated BioContainers addition for mykatlas"
config: {"url": "https://biocontainers.pro/tools/mykatlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mykatlas", "latest": {"0.6.1--py27h21c881e_5": "sha256:dfa4cc640600037079e807b41321a4d81b45c08435b4877e65234b797c1d5f20"}, "tags": {"0.6.1--py27h21c881e_5": "sha256:dfa4cc640600037079e807b41321a4d81b45c08435b4877e65234b797c1d5f20"}, "docker": "quay.io/biocontainers/mykatlas", "aliases": {"atlas": "/usr/local/bin/atlas", "mccortex31": "/usr/local/bin/mccortex31", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mykatlas.
shpc-registry automated BioContainers addition for mykatlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mykatlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mykatlas:0.6.1--py27h21c881e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mykatlas/0.6.1--py27h21c881e_5
$ module help quay.io/biocontainers/mykatlas/0.6.1--py27h21c881e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mykatlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mykatlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mykatlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mykatlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mykatlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mykatlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atlas

```bash
$ singularity exec <container> /usr/local/bin/atlas
$ podman run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mccortex31

```bash
$ singularity exec <container> /usr/local/bin/mccortex31
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex31   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex31   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/metasnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metasnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metasnv/container.yaml"
updated_at: "2023-07-08 03:29:13.213595"
latest: "2.0.4--py39h493604c_6"
container_url: "https://biocontainers.pro/tools/metasnv"
aliases:
 - "metaSNV.py"
 - "metaSNV_DistDiv.py"
 - "metaSNV_Filtering.py"
 - "metaSNV_subpopr.R"
 - "pandoc-server"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "pandoc"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
versions:
 - "2.0.4--py37h47940ae_4"
 - "2.0.4--py39h071e722_5"
 - "2.0.4--py39h493604c_6"
description: "shpc-registry automated BioContainers addition for metasnv"
config: {"url": "https://biocontainers.pro/tools/metasnv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metasnv", "latest": {"2.0.4--py39h493604c_6": "sha256:8d789d7352b59b57fc4d8969b0168c44e7287f53d906c4f3087d6153edf27122"}, "tags": {"2.0.4--py37h47940ae_4": "sha256:b6e0ebfa3b6260e5e05d5a9382608ee99db96f65e7f33df6b498b18e822a5604", "2.0.4--py39h071e722_5": "sha256:32729c179f8bcef130db6c8086933d371d1335e121be2c93969bfb39e6083bab", "2.0.4--py39h493604c_6": "sha256:8d789d7352b59b57fc4d8969b0168c44e7287f53d906c4f3087d6153edf27122"}, "docker": "quay.io/biocontainers/metasnv", "aliases": {"metaSNV.py": "/usr/local/bin/metaSNV.py", "metaSNV_DistDiv.py": "/usr/local/bin/metaSNV_DistDiv.py", "metaSNV_Filtering.py": "/usr/local/bin/metaSNV_Filtering.py", "metaSNV_subpopr.R": "/usr/local/bin/metaSNV_subpopr.R", "pandoc-server": "/usr/local/bin/pandoc-server", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "pandoc": "/usr/local/bin/pandoc", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metasnv.
shpc-registry automated BioContainers addition for metasnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metasnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metasnv:2.0.4--py39h493604c_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metasnv/2.0.4--py39h493604c_6
$ module help quay.io/biocontainers/metasnv/2.0.4--py39h493604c_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metasnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metasnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metasnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metasnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metasnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metasnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaSNV.py

```bash
$ singularity exec <container> /usr/local/bin/metaSNV.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaSNV_DistDiv.py

```bash
$ singularity exec <container> /usr/local/bin/metaSNV_DistDiv.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV_DistDiv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV_DistDiv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaSNV_Filtering.py

```bash
$ singularity exec <container> /usr/local/bin/metaSNV_Filtering.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV_Filtering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV_Filtering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaSNV_subpopr.R

```bash
$ singularity exec <container> /usr/local/bin/metaSNV_subpopr.R
$ podman run --it --rm --entrypoint /usr/local/bin/metaSNV_subpopr.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaSNV_subpopr.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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
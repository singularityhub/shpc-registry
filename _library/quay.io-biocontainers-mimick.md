---
layout: container
name:  "quay.io/biocontainers/mimick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimick/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mimick/container.yaml"
updated_at: "2025-11-24 04:17:22.732262"
latest: "2.3--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/mimick"
aliases:
 - "mimick"
 - "pywgsim"
 - "rich-click"
 - "plac_runner.py"
 - "annot-tsv"
 - "markdown-it"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "numpy-config"
 - "pygmentize"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.1--pyhdfd78af_1"
 - "1.1.0--pyhdfd78af_1"
 - "1.0.2--pyhdfd78af_0"
 - "2.0--pyhdfd78af_0"
 - "1.3--pyhdfd78af_0"
 - "1.2.1--pyhdfd78af_0"
 - "2.3--pyh7e72e81_0"
 - "2.2.2--pyh7e72e81_0"
 - "2.1--pyh7e72e81_0"
 - "2.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mimick"
config: {"url": "https://biocontainers.pro/tools/mimick", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mimick", "latest": {"2.3--pyh7e72e81_0": "sha256:8dba8526fba0b3cb3e01a889286ab06f80317847fa7f884f057b62ccf0790975"}, "tags": {"1.0.1--pyhdfd78af_1": "sha256:50e6478e3132b78e7548e7ccd3a2c5eccfe857fc50bad8d1e2aa858868706420", "1.1.0--pyhdfd78af_1": "sha256:29777c82dcc5cb39e9ba9fed802a1463ad7605908ac2ced9cc0a0420b2a85cda", "1.0.2--pyhdfd78af_0": "sha256:8d09918b2aaf9c3c1edc327e7640b3446c9aefd6acdfd5bde83c5f77fc63e477", "2.0--pyhdfd78af_0": "sha256:5bb2aed64f67a31d1ef1ddf60f4853582eb773130b0fb76f81ecfae70204ed2b", "1.3--pyhdfd78af_0": "sha256:2ed3b91d1e19ec432b6579e1d60d12a5998c89026d3f69ba780be84929916c0e", "1.2.1--pyhdfd78af_0": "sha256:c71a613479fd15712b6226715101a1b76cae28d0344dc425360b721f1b1c5d8a", "2.3--pyh7e72e81_0": "sha256:8dba8526fba0b3cb3e01a889286ab06f80317847fa7f884f057b62ccf0790975", "2.2.2--pyh7e72e81_0": "sha256:891177d2cb6cc594dea6029b12b3854312ba573385a621436ddd1122e19a4417", "2.1--pyh7e72e81_0": "sha256:565aaa6af98d6159560e6150a07e33f539c86ca14b422854ecfb09e21a709d22", "2.0.1--pyhdfd78af_0": "sha256:959b3c2e501117ff802588f9fde22549eeb21f7e6477e6749c7c8fe2f63b7b9f"}, "docker": "quay.io/biocontainers/mimick", "aliases": {"mimick": "/usr/local/bin/mimick", "pywgsim": "/usr/local/bin/pywgsim", "rich-click": "/usr/local/bin/rich-click", "plac_runner.py": "/usr/local/bin/plac_runner.py", "annot-tsv": "/usr/local/bin/annot-tsv", "markdown-it": "/usr/local/bin/markdown-it", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "numpy-config": "/usr/local/bin/numpy-config", "pygmentize": "/usr/local/bin/pygmentize", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimick.
singularity registry hpc automated addition for mimick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimick:2.3--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimick/2.3--pyh7e72e81_0
$ module help quay.io/biocontainers/mimick/2.3--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mimick

```bash
$ singularity exec <container> /usr/local/bin/mimick
$ podman run --it --rm --entrypoint /usr/local/bin/mimick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pywgsim

```bash
$ singularity exec <container> /usr/local/bin/pywgsim
$ podman run --it --rm --entrypoint /usr/local/bin/pywgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pywgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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
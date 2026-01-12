---
layout: container
name:  "quay.io/biocontainers/haproh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haproh/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haproh/container.yaml"
updated_at: "2026-01-12 04:02:29.551999"
latest: "0.64--py310h1fe012e_4"
container_url: "https://biocontainers.pro/tools/haproh"
aliases:
 - "hapConX"
 - "hapCon_ROH"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
versions:
 - "0.60--py39hbf8eff0_0"
 - "0.62--py39hbf8eff0_0"
 - "0.63--py39hbf8eff0_0"
 - "0.64--py36h91eb985_0"
 - "0.64--py39hf95cd2a_1"
 - "0.64--py310h4b81fae_1"
 - "0.63--py310h1425a21_0"
 - "0.62--py310h1425a21_0"
 - "0.60--py310h1425a21_0"
 - "0.64--py311hdad781d_2"
 - "0.64--py311haab0aaa_3"
 - "0.64--py310h1fe012e_4"
description: "shpc-registry automated BioContainers addition for haproh"
config: {"url": "https://biocontainers.pro/tools/haproh", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haproh", "latest": {"0.64--py310h1fe012e_4": "sha256:a66f9e9a3bf6ae1d739de96773aea72cd5c68b7fbed74aea63b967f0db001115"}, "tags": {"0.60--py39hbf8eff0_0": "sha256:f59dc5082b18cc53e74e0ea15082e33996216861f89596b7ccb2d287bea4bcce", "0.62--py39hbf8eff0_0": "sha256:8da266faf28ba2281ebbab2ce722f7379aef0f489cd730d9d34f9c9965767779", "0.63--py39hbf8eff0_0": "sha256:9e65f0df58e26e4ac5b20ac864143d83e43d525766a1f79a39b9090fca02d658", "0.64--py36h91eb985_0": "sha256:add733f72bdb924f89678caaa7ae416d94178ca84daf4faa5ee52c8393cc731c", "0.64--py39hf95cd2a_1": "sha256:434135142641bf8934623778ba175ff7ff1a1a215881cbecf1e7ddf97e94425d", "0.64--py310h4b81fae_1": "sha256:7d81b6b1c77fc1b612442a31a3a23a55da78f175b8db24d3822209848096a3ff", "0.63--py310h1425a21_0": "sha256:4831b94eb7fda668005abc559e376f762871fbc3fdc891a0282a55555b37e10b", "0.62--py310h1425a21_0": "sha256:18da28d8c17b6d5d195cea8a17516debfcb17d3fda1f57670c957e844345f67d", "0.60--py310h1425a21_0": "sha256:1eefef9469e589657bd0a586801a44f4a5325759e526c6192803d77408e4d523", "0.64--py311hdad781d_2": "sha256:2e6545702d7bb7f212866d234a02094a962897cae94cb0445d7bfa97756775be", "0.64--py311haab0aaa_3": "sha256:b8755d33f958299bfbc4dcfceda95fbd7b9d3ddb4881b109c216ecf94b0e4a89", "0.64--py310h1fe012e_4": "sha256:a66f9e9a3bf6ae1d739de96773aea72cd5c68b7fbed74aea63b967f0db001115"}, "docker": "quay.io/biocontainers/haproh", "aliases": {"hapConX": "/usr/local/bin/hapConX", "hapCon_ROH": "/usr/local/bin/hapCon_ROH", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haproh.
shpc-registry automated BioContainers addition for haproh
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haproh
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haproh:0.64--py310h1fe012e_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haproh/0.64--py310h1fe012e_4
$ module help quay.io/biocontainers/haproh/0.64--py310h1fe012e_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haproh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haproh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haproh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haproh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haproh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haproh-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hapConX

```bash
$ singularity exec <container> /usr/local/bin/hapConX
$ podman run --it --rm --entrypoint /usr/local/bin/hapConX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapConX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapCon_ROH

```bash
$ singularity exec <container> /usr/local/bin/hapCon_ROH
$ podman run --it --rm --entrypoint /usr/local/bin/hapCon_ROH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapCon_ROH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
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
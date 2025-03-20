---
layout: container
name:  "quay.io/biocontainers/ppanggolin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ppanggolin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ppanggolin/container.yaml"
updated_at: "2025-03-20 03:02:23.315354"
latest: "2.2.1--py310h1fe012e_2"
container_url: "https://biocontainers.pro/tools/ppanggolin"
aliases:
 - "gawk-5.0.1"
 - "ppanggolin"
 - "mmseqs"
 - "aragorn"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
versions:
 - "v0.3.88--py36h516909a_1"
 - "1.2.74--py38hbff2b2d_1"
 - "1.1.136--py37h73a75cf_1"
 - "1.0.13--py36h516909a_0"
 - "1.2.105--py39hbf8eff0_0"
 - "1.2.105--py310h4b81fae_1"
 - "2.1.0--py39hff71179_0"
 - "2.0.5--py38h0020b31_1"
 - "1.2.105--py38he5da3d1_1"
 - "1.1.136--py36hc5360cc_1"
 - "2.1.1--py39hff71179_0"
 - "2.1.2--py312hf67a6ed_1"
 - "2.2.0--py39hff71179_0"
 - "2.2.1--py310h1fe012e_1"
 - "2.2.1--py310h1fe012e_2"
description: "shpc-registry automated BioContainers addition for ppanggolin"
config: {"url": "https://biocontainers.pro/tools/ppanggolin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ppanggolin", "latest": {"2.2.1--py310h1fe012e_2": "sha256:4f791747442daef8b56b433889157fdb6490a1d88f476b9e5a538249c30cc380"}, "tags": {"v0.3.88--py36h516909a_1": "sha256:24940dd298e4db3cd4a99d26b23835b218cb7a5c03cdfb7b5e285bf5d4dbeba2", "1.2.74--py38hbff2b2d_1": "sha256:cc90238050f7954da4ba0da234a309675acd1b22c55e750b98ac63ba1e537fc3", "1.1.136--py37h73a75cf_1": "sha256:ac677fcb63237c628d8a6d0004eed60b2493919a61402e630f502106e76288c6", "1.0.13--py36h516909a_0": "sha256:de0b3cffdf6beb6c3e7fa6c4dbfab675b80f27cd2c012c8205c59fc9490546d2", "1.2.105--py39hbf8eff0_0": "sha256:866d8c387968084e15160ec5e0d9602a4896709bd802a9800e4b0c8c0b42f2ac", "1.2.105--py310h4b81fae_1": "sha256:3d6f75af210f47a192485e94f4a2a7eac228036975023306532f70282285a24b", "2.1.0--py39hff71179_0": "sha256:f578867a62c36caaedb6880b2320143707968413dcc470a6c6203dd2d525a198", "2.0.5--py38h0020b31_1": "sha256:5e3f2aaeb1c6b0d7c216e08b4fe9cb1ed024aa732d4f3376878bdbcb90322225", "1.2.105--py38he5da3d1_1": "sha256:227084d71ec7e64dc10ed4c1d3e4807853299af8035e92ff495113f7d3e89875", "1.1.136--py36hc5360cc_1": "sha256:6bbcfcb11671f7e3a0eb2c932ac60447da22f6dbbce6ef6f3df7d0da15217269", "2.1.1--py39hff71179_0": "sha256:38218b26e6edfb251dbf2373f7005180e47476ab4a615851c981ed85c0a31360", "2.1.2--py312hf67a6ed_1": "sha256:431a58128ec126e6d7720e9acc4208eb8eb7f7783294f4be2786878126c896c8", "2.2.0--py39hff71179_0": "sha256:66f3ab5246922ba34c584acce57588b8a3f08aa046f1e2e46fdf6e47f62bf2be", "2.2.1--py310h1fe012e_1": "sha256:501f0673fff4ad800d6333648824293337f27bae5ea2b25fc9ae7425bf769e10", "2.2.1--py310h1fe012e_2": "sha256:4f791747442daef8b56b433889157fdb6490a1d88f476b9e5a538249c30cc380"}, "docker": "quay.io/biocontainers/ppanggolin", "aliases": {"gawk-5.0.1": "/usr/local/bin/gawk-5.0.1", "ppanggolin": "/usr/local/bin/ppanggolin", "mmseqs": "/usr/local/bin/mmseqs", "aragorn": "/usr/local/bin/aragorn", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ppanggolin.
shpc-registry automated BioContainers addition for ppanggolin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ppanggolin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ppanggolin:2.2.1--py310h1fe012e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ppanggolin/2.2.1--py310h1fe012e_2
$ module help quay.io/biocontainers/ppanggolin/2.2.1--py310h1fe012e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ppanggolin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ppanggolin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ppanggolin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ppanggolin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.0.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.0.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanggolin

```bash
$ singularity exec <container> /usr/local/bin/ppanggolin
$ podman run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
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
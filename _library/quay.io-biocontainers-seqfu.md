---
layout: container
name:  "quay.io/biocontainers/seqfu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqfu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqfu/container.yaml"
updated_at: "2025-03-16 03:07:57.120828"
latest: "1.22.3--hc29b5fc_1"
container_url: "https://biocontainers.pro/tools/seqfu"
aliases:
 - "dadaist2-mergeseqs"
 - "fu-16Sregion"
 - "fu-cov"
 - "fu-homocomp"
 - "fu-index"
 - "fu-msa"
 - "fu-multirelabel"
 - "fu-nanotags"
 - "fu-orf"
 - "fu-primers"
 - "fu-shred"
 - "fu-sw"
 - "fu-tabcheck"
 - "fu-virfilter"
 - "seqfu"
versions:
 - "1.9.1--h38613fd_0"
 - "1.20.3--h1eb128b_0"
 - "1.18.0--h6ead514_0"
 - "1.17.1--h6ead514_2"
 - "1.16.0--hbd632db_0"
 - "1.15.3--hbd632db_0"
 - "1.20.3--h1eb128b_1"
 - "1.20.3--h1eb128b_2"
 - "1.22.0--h1eb128b_0"
 - "1.22.3--h1eb128b_0"
 - "1.22.3--hc29b5fc_1"
description: "shpc-registry automated BioContainers addition for seqfu"
config: {"url": "https://biocontainers.pro/tools/seqfu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqfu", "latest": {"1.22.3--hc29b5fc_1": "sha256:a1f68fe6a9255457bfed8cb10b263524b9f7124d10ac424b1b8a3330758821fa"}, "tags": {"1.9.1--h38613fd_0": "sha256:41311b69fd24c9da0ad9213cee97efc34bb4a87b196fbc5c79204182dfab4865", "1.20.3--h1eb128b_0": "sha256:8a748c805f226b5c66473b139100fff36d6cc5b1cdff7d5cfa45b51b9e3bd47e", "1.18.0--h6ead514_0": "sha256:cab09b6e20820caf824c28b2835fd8942efb3f7e813ba08afd0bec99b30b4ac0", "1.17.1--h6ead514_2": "sha256:ef997cedffedc74e61a308367dfaaaf73c91435af644f0bfe318e3574089c626", "1.16.0--hbd632db_0": "sha256:58f274071d6352da738fa5e2f77c61f1404ab71956effb7e89ade1fa9316a897", "1.15.3--hbd632db_0": "sha256:1ffcf63e0464d1ce2720b25b1e52c43c419f1aff2aec1b4dbe1814ecca993de1", "1.20.3--h1eb128b_1": "sha256:6db33aec797a36202eac7b03623bd17f0238dcb80e50c2e4f86bfc9678796f9c", "1.20.3--h1eb128b_2": "sha256:6fb86161b4b29b876253dfe4c72f8620801dfc8b905e9ed026c9386aef3b62e1", "1.22.0--h1eb128b_0": "sha256:c00b1b4458ac46d69e3a54dafe5d29c7274c1f46549b461257c1947457804991", "1.22.3--h1eb128b_0": "sha256:a0088c2021fd64b5b8f942330f9a4a7d191cbe5093e7392d19eea7bb1e453ad3", "1.22.3--hc29b5fc_1": "sha256:a1f68fe6a9255457bfed8cb10b263524b9f7124d10ac424b1b8a3330758821fa"}, "docker": "quay.io/biocontainers/seqfu", "aliases": {"dadaist2-mergeseqs": "/usr/local/bin/dadaist2-mergeseqs", "fu-16Sregion": "/usr/local/bin/fu-16Sregion", "fu-cov": "/usr/local/bin/fu-cov", "fu-homocomp": "/usr/local/bin/fu-homocomp", "fu-index": "/usr/local/bin/fu-index", "fu-msa": "/usr/local/bin/fu-msa", "fu-multirelabel": "/usr/local/bin/fu-multirelabel", "fu-nanotags": "/usr/local/bin/fu-nanotags", "fu-orf": "/usr/local/bin/fu-orf", "fu-primers": "/usr/local/bin/fu-primers", "fu-shred": "/usr/local/bin/fu-shred", "fu-sw": "/usr/local/bin/fu-sw", "fu-tabcheck": "/usr/local/bin/fu-tabcheck", "fu-virfilter": "/usr/local/bin/fu-virfilter", "seqfu": "/usr/local/bin/seqfu"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqfu.
shpc-registry automated BioContainers addition for seqfu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqfu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqfu:1.22.3--hc29b5fc_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqfu/1.22.3--hc29b5fc_1
$ module help quay.io/biocontainers/seqfu/1.22.3--hc29b5fc_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqfu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqfu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqfu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqfu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqfu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqfu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dadaist2-mergeseqs

```bash
$ singularity exec <container> /usr/local/bin/dadaist2-mergeseqs
$ podman run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-16Sregion

```bash
$ singularity exec <container> /usr/local/bin/fu-16Sregion
$ podman run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-cov

```bash
$ singularity exec <container> /usr/local/bin/fu-cov
$ podman run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-homocomp

```bash
$ singularity exec <container> /usr/local/bin/fu-homocomp
$ podman run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-index

```bash
$ singularity exec <container> /usr/local/bin/fu-index
$ podman run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-msa

```bash
$ singularity exec <container> /usr/local/bin/fu-msa
$ podman run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-multirelabel

```bash
$ singularity exec <container> /usr/local/bin/fu-multirelabel
$ podman run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-nanotags

```bash
$ singularity exec <container> /usr/local/bin/fu-nanotags
$ podman run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-orf

```bash
$ singularity exec <container> /usr/local/bin/fu-orf
$ podman run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-primers

```bash
$ singularity exec <container> /usr/local/bin/fu-primers
$ podman run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-shred

```bash
$ singularity exec <container> /usr/local/bin/fu-shred
$ podman run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-sw

```bash
$ singularity exec <container> /usr/local/bin/fu-sw
$ podman run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-tabcheck

```bash
$ singularity exec <container> /usr/local/bin/fu-tabcheck
$ podman run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-virfilter

```bash
$ singularity exec <container> /usr/local/bin/fu-virfilter
$ podman run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqfu

```bash
$ singularity exec <container> /usr/local/bin/seqfu
$ podman run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
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
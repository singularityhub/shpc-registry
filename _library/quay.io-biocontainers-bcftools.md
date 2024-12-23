---
layout: container
name:  "quay.io/biocontainers/bcftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcftools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bcftools/container.yaml"
updated_at: "2024-12-23 03:19:22.689577"
latest: "1.21--h3a4d415_1"
container_url: "https://biocontainers.pro/tools/bcftools"
aliases:
 - "bcftools"
 - "bgzip"
 - "color-chrs.pl"
 - "gff2gff.py"
 - "guess-ploidy.py"
 - "htsfile"
 - "libdeflate-gunzip"
 - "libdeflate-gzip"
 - "plot-roh.py"
 - "plot-vcfstats"
 - "run-roh.pl"
 - "tabix"
 - "vcfutils.pl"
versions:
 - "1.12--h45bccc9_1"
 - "1.13--h3a49de5_0"
 - "1.14--h88f3f91_0"
 - "1.15--haf5b3da_0"
 - "1.19--h8b25389_1"
 - "1.18--h8b25389_0"
 - "1.17--h3cc50cf_1"
 - "1.16--haef29d1_2"
 - "1.15--h0ea216a_2"
 - "1.20--h8b25389_0"
 - "1.20--h8b25389_1"
 - "1.21--h8b25389_0"
 - "1.21--h3a4d415_1"
description: "shpc-registry automated BioContainers addition for bcftools"
config: {"url": "https://biocontainers.pro/tools/bcftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcftools", "latest": {"1.21--h3a4d415_1": "sha256:e32f39e2c692c4a6ec8ba4a48b1f9b5b6c01616aba46affdaca0b943014e794e"}, "tags": {"1.12--h45bccc9_1": "sha256:46e9e8527167c0394a99a5f0f964c8af771f8349140062a3a2d32b1e348a9bf0", "1.13--h3a49de5_0": "sha256:4eba5e6d3083a3e5c858bedb98d2148b0b27b3182c2462e82905721065bf4962", "1.14--h88f3f91_0": "sha256:1da62c4e5facf6c6186cabec8ad5320f52ed0845d0f3102e80d68fc1832f4a61", "1.15--haf5b3da_0": "sha256:139465dc94f46e08600b5285602bdb3a363b683271dbab3b397618edc654719c", "1.19--h8b25389_1": "sha256:23ce108d4da990e9140a8a762907d84bed1c3831f040dde3b1e3b67ec9cca748", "1.18--h8b25389_0": "sha256:f3497f167d499a90db55f2c82b3d93ebe06bbaa85760883b323cc2bb0123658e", "1.17--h3cc50cf_1": "sha256:e05214bfea4fb3c8c202985702b4d5e9fbec03e34af2935bcf2ce353776324e9", "1.16--haef29d1_2": "sha256:9977e777f94473f9dd47339b138b155abe21f1f019ef525214f13186fafbf65d", "1.15--h0ea216a_2": "sha256:bdb29cbb48040c6832e066244721026fd72f87875198685b89041e90f568f78e", "1.20--h8b25389_0": "sha256:badc3a0c7af72a83e5761ab0e881aa84204694bdead003b47552cb283958f78d", "1.20--h8b25389_1": "sha256:9b2203c6bc5a3effb41555e66dbc1ad727827706db3fa8aa60134e9cf84f4763", "1.21--h8b25389_0": "sha256:969314d56b9131683917cc5801734891a9af130daf7a0fb902b7707060b06027", "1.21--h3a4d415_1": "sha256:e32f39e2c692c4a6ec8ba4a48b1f9b5b6c01616aba46affdaca0b943014e794e"}, "docker": "quay.io/biocontainers/bcftools", "aliases": {"bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "gff2gff.py": "/usr/local/bin/gff2gff.py", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "htsfile": "/usr/local/bin/htsfile", "libdeflate-gunzip": "/usr/local/bin/libdeflate-gunzip", "libdeflate-gzip": "/usr/local/bin/libdeflate-gzip", "plot-roh.py": "/usr/local/bin/plot-roh.py", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "run-roh.pl": "/usr/local/bin/run-roh.pl", "tabix": "/usr/local/bin/tabix", "vcfutils.pl": "/usr/local/bin/vcfutils.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcftools.
shpc-registry automated BioContainers addition for bcftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcftools:1.21--h3a4d415_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcftools/1.21--h3a4d415_1
$ module help quay.io/biocontainers/bcftools/1.21--h3a4d415_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libdeflate-gunzip

```bash
$ singularity exec <container> /usr/local/bin/libdeflate-gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/libdeflate-gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libdeflate-gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libdeflate-gzip

```bash
$ singularity exec <container> /usr/local/bin/libdeflate-gzip
$ podman run --it --rm --entrypoint /usr/local/bin/libdeflate-gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libdeflate-gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
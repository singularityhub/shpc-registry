---
layout: container
name:  "quay.io/biocontainers/bcftools-gtc2vcf-plugin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcftools-gtc2vcf-plugin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bcftools-gtc2vcf-plugin/container.yaml"
updated_at: "2025-10-02 03:43:17.328325"
latest: "1.22--hb66fcc3_0"
container_url: "https://biocontainers.pro/tools/bcftools-gtc2vcf-plugin"
aliases:
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
versions:
 - "1.9--hedc5323_0"
 - "1.19--h4dfc31f_0"
 - "1.18--h4dfc31f_0"
 - "1.19--h4dfc31f_1"
 - "1.21--hb66fcc3_0"
 - "1.22--hb66fcc3_0"
description: "shpc-registry automated BioContainers addition for bcftools-gtc2vcf-plugin"
config: {"url": "https://biocontainers.pro/tools/bcftools-gtc2vcf-plugin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcftools-gtc2vcf-plugin", "latest": {"1.22--hb66fcc3_0": "sha256:21df2f3361cf8858265c3b838e26fe06768839cba41216e47438242b621d17af"}, "tags": {"1.9--hedc5323_0": "sha256:6bac9c4b21bdd4da8c7e8748bc598301dddd84f6ba2cbf2efe000407a3e54863", "1.19--h4dfc31f_0": "sha256:7804abd6ca13359aeffd7f96de3f6294e7d1b947a059ab2e8078cb1e99d6c688", "1.18--h4dfc31f_0": "sha256:ffd0217f26bf3dd19344d8e46f40b6c5a5e161795f934571dab88ea1b911ad2a", "1.19--h4dfc31f_1": "sha256:28be9423834d565c92ba7f58afab2b7c19f77cf23d7d6c4fb1e2a3e92d9a4fef", "1.21--hb66fcc3_0": "sha256:7a928ddc6e03f066736ddb245c7e546efc77c67d7973d5a1c94bf39c67af73ce", "1.22--hb66fcc3_0": "sha256:21df2f3361cf8858265c3b838e26fe06768839cba41216e47438242b621d17af"}, "docker": "quay.io/biocontainers/bcftools-gtc2vcf-plugin", "aliases": {"guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcftools-gtc2vcf-plugin.
shpc-registry automated BioContainers addition for bcftools-gtc2vcf-plugin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcftools-gtc2vcf-plugin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcftools-gtc2vcf-plugin:1.22--hb66fcc3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcftools-gtc2vcf-plugin/1.22--hb66fcc3_0
$ module help quay.io/biocontainers/bcftools-gtc2vcf-plugin/1.22--hb66fcc3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcftools-gtc2vcf-plugin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-gtc2vcf-plugin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-gtc2vcf-plugin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcftools-gtc2vcf-plugin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcftools-gtc2vcf-plugin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcftools-gtc2vcf-plugin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
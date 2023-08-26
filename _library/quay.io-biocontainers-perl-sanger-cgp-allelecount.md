---
layout: container
name:  "quay.io/biocontainers/perl-sanger-cgp-allelecount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sanger-cgp-allelecount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sanger-cgp-allelecount/container.yaml"
updated_at: "2023-08-26 02:49:05.497247"
latest: "4.3.0--pl5321h031d066_1"
container_url: "https://biocontainers.pro/tools/perl-sanger-cgp-allelecount"
aliases:
 - "alleleCounter.pl"
 - "alleleCounterToJson.pl"
 - "cgpAppendIdsToVcf.pl"
 - "cgpVCFSplit.pl"
 - "cover"
 - "cpancover"
 - "gcov2perl"
 - "tab-to-vcf"
 - "vcf-haplotypes"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
versions:
 - "4.3.0--pl5321hec16e2b_0"
 - "4.3.0--pl5321h031d066_1"
description: "shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount"
config: {"url": "https://biocontainers.pro/tools/perl-sanger-cgp-allelecount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount", "latest": {"4.3.0--pl5321h031d066_1": "sha256:14a04ee083efefc4a3ef6dda9d3139c58d77ddac2c9927b371db87b71f8506dc"}, "tags": {"4.3.0--pl5321hec16e2b_0": "sha256:4a195d434a067d25cdc60f94adf8452ae91b7f3748829e206d2b35297d03d7e2", "4.3.0--pl5321h031d066_1": "sha256:14a04ee083efefc4a3ef6dda9d3139c58d77ddac2c9927b371db87b71f8506dc"}, "docker": "quay.io/biocontainers/perl-sanger-cgp-allelecount", "aliases": {"alleleCounter.pl": "/usr/local/bin/alleleCounter.pl", "alleleCounterToJson.pl": "/usr/local/bin/alleleCounterToJson.pl", "cgpAppendIdsToVcf.pl": "/usr/local/bin/cgpAppendIdsToVcf.pl", "cgpVCFSplit.pl": "/usr/local/bin/cgpVCFSplit.pl", "cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "gcov2perl": "/usr/local/bin/gcov2perl", "tab-to-vcf": "/usr/local/bin/tab-to-vcf", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sanger-cgp-allelecount.
shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-allelecount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-allelecount:4.3.0--pl5321h031d066_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sanger-cgp-allelecount/4.3.0--pl5321h031d066_1
$ module help quay.io/biocontainers/perl-sanger-cgp-allelecount/4.3.0--pl5321h031d066_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sanger-cgp-allelecount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-allelecount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-allelecount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sanger-cgp-allelecount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sanger-cgp-allelecount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sanger-cgp-allelecount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alleleCounter.pl

```bash
$ singularity exec <container> /usr/local/bin/alleleCounter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alleleCounterToJson.pl

```bash
$ singularity exec <container> /usr/local/bin/alleleCounterToJson.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounterToJson.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounterToJson.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpAppendIdsToVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpAppendIdsToVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpVCFSplit.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpVCFSplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpancover

```bash
$ singularity exec <container> /usr/local/bin/cpancover
$ podman run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov2perl

```bash
$ singularity exec <container> /usr/local/bin/gcov2perl
$ podman run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tab-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/tab-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-haplotypes

```bash
$ singularity exec <container> /usr/local/bin/vcf-haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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
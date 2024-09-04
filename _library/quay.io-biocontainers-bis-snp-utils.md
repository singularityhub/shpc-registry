---
layout: container
name:  "quay.io/biocontainers/bis-snp-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bis-snp-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bis-snp-utils/container.yaml"
updated_at: "2024-09-04 03:28:17.838293"
latest: "0.0.1--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bis-snp-utils"
aliases:
 - "annotateBed_2way.pl"
 - "mergeBamWithSameSM.pl"
 - "sep_line_by_name.pl"
 - "sortByRefAndCor.pl"
 - "uniqLine.pl"
 - "vcf2bed.NOME.pl"
 - "vcf2bed.pl"
 - "vcf2bed6plus2.pl"
 - "vcf2bed6plus2.strand.pl"
 - "vcf2bedGraph.pl"
 - "vcf2coverage.pl"
 - "vcf2wig.pl"
 - "vcf2wig_ct_coverage.pl"
 - "vcf4ToRod_in_specific_pos.pl"
 - "gtf2bed.pl"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "0.0.1--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bis-snp-utils"
config: {"url": "https://biocontainers.pro/tools/bis-snp-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bis-snp-utils", "latest": {"0.0.1--hdfd78af_4": "sha256:64cf2d3bf4463bc7d66e2b7389c4cd1bb7d1025bc55fe3fef3a8315d8d97acd9"}, "tags": {"0.0.1--hdfd78af_4": "sha256:64cf2d3bf4463bc7d66e2b7389c4cd1bb7d1025bc55fe3fef3a8315d8d97acd9"}, "docker": "quay.io/biocontainers/bis-snp-utils", "aliases": {"annotateBed_2way.pl": "/usr/local/bin/annotateBed_2way.pl", "mergeBamWithSameSM.pl": "/usr/local/bin/mergeBamWithSameSM.pl", "sep_line_by_name.pl": "/usr/local/bin/sep_line_by_name.pl", "sortByRefAndCor.pl": "/usr/local/bin/sortByRefAndCor.pl", "uniqLine.pl": "/usr/local/bin/uniqLine.pl", "vcf2bed.NOME.pl": "/usr/local/bin/vcf2bed.NOME.pl", "vcf2bed.pl": "/usr/local/bin/vcf2bed.pl", "vcf2bed6plus2.pl": "/usr/local/bin/vcf2bed6plus2.pl", "vcf2bed6plus2.strand.pl": "/usr/local/bin/vcf2bed6plus2.strand.pl", "vcf2bedGraph.pl": "/usr/local/bin/vcf2bedGraph.pl", "vcf2coverage.pl": "/usr/local/bin/vcf2coverage.pl", "vcf2wig.pl": "/usr/local/bin/vcf2wig.pl", "vcf2wig_ct_coverage.pl": "/usr/local/bin/vcf2wig_ct_coverage.pl", "vcf4ToRod_in_specific_pos.pl": "/usr/local/bin/vcf4ToRod_in_specific_pos.pl", "gtf2bed.pl": "/usr/local/bin/gtf2bed.pl", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bis-snp-utils.
shpc-registry automated BioContainers addition for bis-snp-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bis-snp-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bis-snp-utils:0.0.1--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bis-snp-utils/0.0.1--hdfd78af_4
$ module help quay.io/biocontainers/bis-snp-utils/0.0.1--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bis-snp-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bis-snp-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bis-snp-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bis-snp-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bis-snp-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bis-snp-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotateBed_2way.pl

```bash
$ singularity exec <container> /usr/local/bin/annotateBed_2way.pl
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed_2way.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed_2way.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeBamWithSameSM.pl

```bash
$ singularity exec <container> /usr/local/bin/mergeBamWithSameSM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mergeBamWithSameSM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeBamWithSameSM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sep_line_by_name.pl

```bash
$ singularity exec <container> /usr/local/bin/sep_line_by_name.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sep_line_by_name.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sep_line_by_name.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortByRefAndCor.pl

```bash
$ singularity exec <container> /usr/local/bin/sortByRefAndCor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sortByRefAndCor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortByRefAndCor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniqLine.pl

```bash
$ singularity exec <container> /usr/local/bin/uniqLine.pl
$ podman run --it --rm --entrypoint /usr/local/bin/uniqLine.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniqLine.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed.NOME.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed.NOME.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed.NOME.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed.NOME.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed6plus2.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed6plus2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed6plus2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed6plus2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed6plus2.strand.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed6plus2.strand.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed6plus2.strand.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed6plus2.strand.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bedGraph.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bedGraph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bedGraph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bedGraph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2coverage.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2coverage.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2wig.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2wig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2wig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2wig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2wig_ct_coverage.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2wig_ct_coverage.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2wig_ct_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2wig_ct_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf4ToRod_in_specific_pos.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf4ToRod_in_specific_pos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf4ToRod_in_specific_pos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf4ToRod_in_specific_pos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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
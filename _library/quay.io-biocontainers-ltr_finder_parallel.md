---
layout: container
name:  "quay.io/biocontainers/ltr_finder_parallel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ltr_finder_parallel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ltr_finder_parallel/container.yaml"
updated_at: "2025-01-17 03:04:02.806718"
latest: "1.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ltr_finder_parallel"
aliases:
 - "LTR_FINDER_parallel"
 - "check_result.pl"
 - "down_tRNA.pl"
 - "filter_rt.pl"
 - "genome_plot.pl"
 - "genome_plot2.pl"
 - "genome_plot_svg.pl"
 - "ltr_finder"
 - "psearch"
 - "bdf2gdfont.pl"
 - "bdftogd"
 - "gd2copypal"
 - "gd2togif"
 - "gd2topng"
 - "gdcmpgif"
 - "gdparttopng"
 - "gdtopng"
 - "giftogd2"
 - "pngtogd"
 - "pngtogd2"
 - "webpng"
 - "annotate"
 - "tjbench"
 - "img2webp"
 - "cwebp"
 - "dwebp"
 - "gif2webp"
 - "gif2rgb"
 - "gifbuild"
 - "gifclrmp"
 - "giffix"
 - "giftext"
 - "giftool"
versions:
 - "1.1--hdfd78af_0"
 - "1.1--hdfd78af_1"
description: "singularity registry hpc automated addition for ltr_finder_parallel"
config: {"url": "https://biocontainers.pro/tools/ltr_finder_parallel", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ltr_finder_parallel", "latest": {"1.1--hdfd78af_1": "sha256:8a7873f711b6ec6af83cf344e81a8497c4af7541bf707a636a23b0dd3fbb87e8"}, "tags": {"1.1--hdfd78af_0": "sha256:97ae0f3dbfcda9ccf248acc3d282bcba82855c5e797e62efbab9f4fcc4b86a12", "1.1--hdfd78af_1": "sha256:8a7873f711b6ec6af83cf344e81a8497c4af7541bf707a636a23b0dd3fbb87e8"}, "docker": "quay.io/biocontainers/ltr_finder_parallel", "aliases": {"LTR_FINDER_parallel": "/usr/local/bin/LTR_FINDER_parallel", "check_result.pl": "/usr/local/bin/check_result.pl", "down_tRNA.pl": "/usr/local/bin/down_tRNA.pl", "filter_rt.pl": "/usr/local/bin/filter_rt.pl", "genome_plot.pl": "/usr/local/bin/genome_plot.pl", "genome_plot2.pl": "/usr/local/bin/genome_plot2.pl", "genome_plot_svg.pl": "/usr/local/bin/genome_plot_svg.pl", "ltr_finder": "/usr/local/bin/ltr_finder", "psearch": "/usr/local/bin/psearch", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl", "bdftogd": "/usr/local/bin/bdftogd", "gd2copypal": "/usr/local/bin/gd2copypal", "gd2togif": "/usr/local/bin/gd2togif", "gd2topng": "/usr/local/bin/gd2topng", "gdcmpgif": "/usr/local/bin/gdcmpgif", "gdparttopng": "/usr/local/bin/gdparttopng", "gdtopng": "/usr/local/bin/gdtopng", "giftogd2": "/usr/local/bin/giftogd2", "pngtogd": "/usr/local/bin/pngtogd", "pngtogd2": "/usr/local/bin/pngtogd2", "webpng": "/usr/local/bin/webpng", "annotate": "/usr/local/bin/annotate", "tjbench": "/usr/local/bin/tjbench", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "gif2webp": "/usr/local/bin/gif2webp", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp", "giffix": "/usr/local/bin/giffix", "giftext": "/usr/local/bin/giftext", "giftool": "/usr/local/bin/giftool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ltr_finder_parallel.
singularity registry hpc automated addition for ltr_finder_parallel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ltr_finder_parallel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ltr_finder_parallel:1.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ltr_finder_parallel/1.1--hdfd78af_1
$ module help quay.io/biocontainers/ltr_finder_parallel/1.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ltr_finder_parallel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ltr_finder_parallel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ltr_finder_parallel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ltr_finder_parallel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ltr_finder_parallel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ltr_finder_parallel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LTR_FINDER_parallel

```bash
$ singularity exec <container> /usr/local/bin/LTR_FINDER_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_FINDER_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_FINDER_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_result.pl

```bash
$ singularity exec <container> /usr/local/bin/check_result.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### down_tRNA.pl

```bash
$ singularity exec <container> /usr/local/bin/down_tRNA.pl
$ podman run --it --rm --entrypoint /usr/local/bin/down_tRNA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/down_tRNA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_rt.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_rt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_rt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_rt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot2.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot_svg.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot_svg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ltr_finder

```bash
$ singularity exec <container> /usr/local/bin/ltr_finder
$ podman run --it --rm --entrypoint /usr/local/bin/ltr_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ltr_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psearch

```bash
$ singularity exec <container> /usr/local/bin/psearch
$ podman run --it --rm --entrypoint /usr/local/bin/psearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdf2gdfont.pl

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2togif

```bash
$ singularity exec <container> /usr/local/bin/gd2togif
$ podman run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2topng

```bash
$ singularity exec <container> /usr/local/bin/gd2topng
$ podman run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdcmpgif

```bash
$ singularity exec <container> /usr/local/bin/gdcmpgif
$ podman run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdparttopng

```bash
$ singularity exec <container> /usr/local/bin/gdparttopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdtopng

```bash
$ singularity exec <container> /usr/local/bin/gdtopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftogd2

```bash
$ singularity exec <container> /usr/local/bin/giftogd2
$ podman run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd

```bash
$ singularity exec <container> /usr/local/bin/pngtogd
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd2

```bash
$ singularity exec <container> /usr/local/bin/pngtogd2
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webpng

```bash
$ singularity exec <container> /usr/local/bin/webpng
$ podman run --it --rm --entrypoint /usr/local/bin/webpng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webpng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifclrmp

```bash
$ singularity exec <container> /usr/local/bin/gifclrmp
$ podman run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffix

```bash
$ singularity exec <container> /usr/local/bin/giffix
$ podman run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftext

```bash
$ singularity exec <container> /usr/local/bin/giftext
$ podman run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftool

```bash
$ singularity exec <container> /usr/local/bin/giftool
$ podman run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
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
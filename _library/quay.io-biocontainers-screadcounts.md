---
layout: container
name:  "quay.io/biocontainers/screadcounts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/screadcounts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/screadcounts/container.yaml"
updated_at: "2024-04-09 02:38:53.840026"
latest: "1.4.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/screadcounts"
aliases:
 - "helpviewer"
 - "img2png"
 - "img2py"
 - "img2xpm"
 - "pycrust"
 - "pyshell"
 - "pyslices"
 - "pyslicesshell"
 - "pywxrc"
 - "readCounts"
 - "readCountsMatrix"
 - "scReadCounts"
 - "scVarLoci"
 - "varLoci"
 - "wx-config"
 - "wxdemo"
 - "wxdocs"
 - "wxget"
 - "wxrc"
 - "wxrc-3.2"
 - "gtk-builder-convert"
 - "gtk-demo"
 - "gtk-query-immodules-2.0"
 - "gtk-update-icon-cache"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
 - "normalizer"
 - "gst-device-monitor-1.0"
 - "gst-discoverer-1.0"
 - "gst-play-1.0"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "gst-inspect-1.0"
 - "gst-launch-1.0"
 - "gst-stats-1.0"
 - "gst-typefind-1.0"
 - "f2py3.10"
 - "aserver"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "ace2sam"
 - "blast2sam.pl"
versions:
 - "1.3.2--hdfd78af_0"
 - "1.4.0--hdfd78af_0"
description: "singularity registry hpc automated addition for screadcounts"
config: {"url": "https://biocontainers.pro/tools/screadcounts", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for screadcounts", "latest": {"1.4.0--hdfd78af_0": "sha256:086add4dbe78621aba8e60be450838ee978ca2bf11a5f116d61cb630112153c4"}, "tags": {"1.3.2--hdfd78af_0": "sha256:919f4e7f0994a1ee13a27786f8b43e8d15f9737fd7648e9191d3307f9e4d11e1", "1.4.0--hdfd78af_0": "sha256:086add4dbe78621aba8e60be450838ee978ca2bf11a5f116d61cb630112153c4"}, "docker": "quay.io/biocontainers/screadcounts", "aliases": {"helpviewer": "/usr/local/bin/helpviewer", "img2png": "/usr/local/bin/img2png", "img2py": "/usr/local/bin/img2py", "img2xpm": "/usr/local/bin/img2xpm", "pycrust": "/usr/local/bin/pycrust", "pyshell": "/usr/local/bin/pyshell", "pyslices": "/usr/local/bin/pyslices", "pyslicesshell": "/usr/local/bin/pyslicesshell", "pywxrc": "/usr/local/bin/pywxrc", "readCounts": "/usr/local/bin/readCounts", "readCountsMatrix": "/usr/local/bin/readCountsMatrix", "scReadCounts": "/usr/local/bin/scReadCounts", "scVarLoci": "/usr/local/bin/scVarLoci", "varLoci": "/usr/local/bin/varLoci", "wx-config": "/usr/local/bin/wx-config", "wxdemo": "/usr/local/bin/wxdemo", "wxdocs": "/usr/local/bin/wxdocs", "wxget": "/usr/local/bin/wxget", "wxrc": "/usr/local/bin/wxrc", "wxrc-3.2": "/usr/local/bin/wxrc-3.2", "gtk-builder-convert": "/usr/local/bin/gtk-builder-convert", "gtk-demo": "/usr/local/bin/gtk-demo", "gtk-query-immodules-2.0": "/usr/local/bin/gtk-query-immodules-2.0", "gtk-update-icon-cache": "/usr/local/bin/gtk-update-icon-cache", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders", "normalizer": "/usr/local/bin/normalizer", "gst-device-monitor-1.0": "/usr/local/bin/gst-device-monitor-1.0", "gst-discoverer-1.0": "/usr/local/bin/gst-discoverer-1.0", "gst-play-1.0": "/usr/local/bin/gst-play-1.0", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "gst-inspect-1.0": "/usr/local/bin/gst-inspect-1.0", "gst-launch-1.0": "/usr/local/bin/gst-launch-1.0", "gst-stats-1.0": "/usr/local/bin/gst-stats-1.0", "gst-typefind-1.0": "/usr/local/bin/gst-typefind-1.0", "f2py3.10": "/usr/local/bin/f2py3.10", "aserver": "/usr/local/bin/aserver", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/screadcounts.
singularity registry hpc automated addition for screadcounts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/screadcounts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/screadcounts:1.4.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/screadcounts/1.4.0--hdfd78af_0
$ module help quay.io/biocontainers/screadcounts/1.4.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### screadcounts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### screadcounts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### screadcounts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### screadcounts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### screadcounts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### screadcounts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### helpviewer

```bash
$ singularity exec <container> /usr/local/bin/helpviewer
$ podman run --it --rm --entrypoint /usr/local/bin/helpviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/helpviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2png

```bash
$ singularity exec <container> /usr/local/bin/img2png
$ podman run --it --rm --entrypoint /usr/local/bin/img2png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2png   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2py

```bash
$ singularity exec <container> /usr/local/bin/img2py
$ podman run --it --rm --entrypoint /usr/local/bin/img2py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2xpm

```bash
$ singularity exec <container> /usr/local/bin/img2xpm
$ podman run --it --rm --entrypoint /usr/local/bin/img2xpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2xpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycrust

```bash
$ singularity exec <container> /usr/local/bin/pycrust
$ podman run --it --rm --entrypoint /usr/local/bin/pycrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycrust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyshell

```bash
$ singularity exec <container> /usr/local/bin/pyshell
$ podman run --it --rm --entrypoint /usr/local/bin/pyshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyslices

```bash
$ singularity exec <container> /usr/local/bin/pyslices
$ podman run --it --rm --entrypoint /usr/local/bin/pyslices   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyslices   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyslicesshell

```bash
$ singularity exec <container> /usr/local/bin/pyslicesshell
$ podman run --it --rm --entrypoint /usr/local/bin/pyslicesshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyslicesshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pywxrc

```bash
$ singularity exec <container> /usr/local/bin/pywxrc
$ podman run --it --rm --entrypoint /usr/local/bin/pywxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pywxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readCounts

```bash
$ singularity exec <container> /usr/local/bin/readCounts
$ podman run --it --rm --entrypoint /usr/local/bin/readCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readCountsMatrix

```bash
$ singularity exec <container> /usr/local/bin/readCountsMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/readCountsMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readCountsMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scReadCounts

```bash
$ singularity exec <container> /usr/local/bin/scReadCounts
$ podman run --it --rm --entrypoint /usr/local/bin/scReadCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scReadCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scVarLoci

```bash
$ singularity exec <container> /usr/local/bin/scVarLoci
$ podman run --it --rm --entrypoint /usr/local/bin/scVarLoci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scVarLoci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varLoci

```bash
$ singularity exec <container> /usr/local/bin/varLoci
$ podman run --it --rm --entrypoint /usr/local/bin/varLoci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varLoci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wx-config

```bash
$ singularity exec <container> /usr/local/bin/wx-config
$ podman run --it --rm --entrypoint /usr/local/bin/wx-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wx-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxdemo

```bash
$ singularity exec <container> /usr/local/bin/wxdemo
$ podman run --it --rm --entrypoint /usr/local/bin/wxdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxdocs

```bash
$ singularity exec <container> /usr/local/bin/wxdocs
$ podman run --it --rm --entrypoint /usr/local/bin/wxdocs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxdocs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxget

```bash
$ singularity exec <container> /usr/local/bin/wxget
$ podman run --it --rm --entrypoint /usr/local/bin/wxget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxrc

```bash
$ singularity exec <container> /usr/local/bin/wxrc
$ podman run --it --rm --entrypoint /usr/local/bin/wxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxrc-3.2

```bash
$ singularity exec <container> /usr/local/bin/wxrc-3.2
$ podman run --it --rm --entrypoint /usr/local/bin/wxrc-3.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxrc-3.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-convert

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-demo

```bash
$ singularity exec <container> /usr/local/bin/gtk-demo
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-2.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-2.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-update-icon-cache

```bash
$ singularity exec <container> /usr/local/bin/gtk-update-icon-cache
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-thumbnailer

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-thumbnailer
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-csource

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-csource
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-pixdata

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-pixdata
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-query-loaders

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-query-loaders
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-device-monitor-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-device-monitor-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-discoverer-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-discoverer-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-play-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-play-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gst-inspect-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-inspect-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-inspect-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-inspect-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-launch-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-launch-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-launch-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-launch-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-stats-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-stats-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-stats-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-stats-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-typefind-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-typefind-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-typefind-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-typefind-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
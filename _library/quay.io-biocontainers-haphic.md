---
layout: container
name:  "quay.io/biocontainers/haphic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haphic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haphic/container.yaml"
updated_at: "2025-08-17 03:57:04.929600"
latest: "1.0.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/haphic"
aliases:
 - "agp_to_fasta"
 - "combine_groups.py"
 - "convert_gfa_ids.py"
 - "fasta_count_N.py"
 - "fastq_length_filtering.py"
 - "filter_bam"
 - "filter_bam.py"
 - "find_telomeres.py"
 - "gfa_depth_to_bedGraph.py"
 - "global_chaining.py"
 - "groups_to_clusters.py"
 - "haphic"
 - "juicer"
 - "juicer_tools.1.9.9_jcuda.0.8.jar"
 - "mock_agp_file.py"
 - "mock_blast_file.py"
 - "prepare_clusters.py"
 - "remove_singletons.py"
 - "reverse_bed.py"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
 - "hwloc-ps"
 - "lstopo"
 - "lstopo-no-graphics"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.7--hdfd78af_0"
description: "singularity registry hpc automated addition for haphic"
config: {"url": "https://biocontainers.pro/tools/haphic", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for haphic", "latest": {"1.0.7--hdfd78af_0": "sha256:5f0640f1344f15d702233f5e0d247385914593f6e756af070923dcc5e9d5345e"}, "tags": {"1.0.7--hdfd78af_0": "sha256:5f0640f1344f15d702233f5e0d247385914593f6e756af070923dcc5e9d5345e"}, "docker": "quay.io/biocontainers/haphic", "aliases": {"agp_to_fasta": "/usr/local/bin/agp_to_fasta", "combine_groups.py": "/usr/local/bin/combine_groups.py", "convert_gfa_ids.py": "/usr/local/bin/convert_gfa_ids.py", "fasta_count_N.py": "/usr/local/bin/fasta_count_N.py", "fastq_length_filtering.py": "/usr/local/bin/fastq_length_filtering.py", "filter_bam": "/usr/local/bin/filter_bam", "filter_bam.py": "/usr/local/bin/filter_bam.py", "find_telomeres.py": "/usr/local/bin/find_telomeres.py", "gfa_depth_to_bedGraph.py": "/usr/local/bin/gfa_depth_to_bedGraph.py", "global_chaining.py": "/usr/local/bin/global_chaining.py", "groups_to_clusters.py": "/usr/local/bin/groups_to_clusters.py", "haphic": "/usr/local/bin/haphic", "juicer": "/usr/local/bin/juicer", "juicer_tools.1.9.9_jcuda.0.8.jar": "/usr/local/bin/juicer_tools.1.9.9_jcuda.0.8.jar", "mock_agp_file.py": "/usr/local/bin/mock_agp_file.py", "mock_blast_file.py": "/usr/local/bin/mock_blast_file.py", "prepare_clusters.py": "/usr/local/bin/prepare_clusters.py", "remove_singletons.py": "/usr/local/bin/remove_singletons.py", "reverse_bed.py": "/usr/local/bin/reverse_bed.py", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haphic.
singularity registry hpc automated addition for haphic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haphic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haphic:1.0.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haphic/1.0.7--hdfd78af_0
$ module help quay.io/biocontainers/haphic/1.0.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haphic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haphic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haphic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haphic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haphic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haphic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agp_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/agp_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/agp_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agp_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_groups.py

```bash
$ singularity exec <container> /usr/local/bin/combine_groups.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_groups.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_groups.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_gfa_ids.py

```bash
$ singularity exec <container> /usr/local/bin/convert_gfa_ids.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_gfa_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_gfa_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_count_N.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_count_N.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_count_N.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_count_N.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_length_filtering.py

```bash
$ singularity exec <container> /usr/local/bin/fastq_length_filtering.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_length_filtering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_length_filtering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_bam

```bash
$ singularity exec <container> /usr/local/bin/filter_bam
$ podman run --it --rm --entrypoint /usr/local/bin/filter_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_bam.py

```bash
$ singularity exec <container> /usr/local/bin/filter_bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_telomeres.py

```bash
$ singularity exec <container> /usr/local/bin/find_telomeres.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_telomeres.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_telomeres.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_depth_to_bedGraph.py

```bash
$ singularity exec <container> /usr/local/bin/gfa_depth_to_bedGraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_depth_to_bedGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_depth_to_bedGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### global_chaining.py

```bash
$ singularity exec <container> /usr/local/bin/global_chaining.py
$ podman run --it --rm --entrypoint /usr/local/bin/global_chaining.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/global_chaining.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groups_to_clusters.py

```bash
$ singularity exec <container> /usr/local/bin/groups_to_clusters.py
$ podman run --it --rm --entrypoint /usr/local/bin/groups_to_clusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groups_to_clusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haphic

```bash
$ singularity exec <container> /usr/local/bin/haphic
$ podman run --it --rm --entrypoint /usr/local/bin/haphic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haphic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer

```bash
$ singularity exec <container> /usr/local/bin/juicer
$ podman run --it --rm --entrypoint /usr/local/bin/juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_tools.1.9.9_jcuda.0.8.jar

```bash
$ singularity exec <container> /usr/local/bin/juicer_tools.1.9.9_jcuda.0.8.jar
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_tools.1.9.9_jcuda.0.8.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_tools.1.9.9_jcuda.0.8.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mock_agp_file.py

```bash
$ singularity exec <container> /usr/local/bin/mock_agp_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/mock_agp_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mock_agp_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mock_blast_file.py

```bash
$ singularity exec <container> /usr/local/bin/mock_blast_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/mock_blast_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mock_blast_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_clusters.py

```bash
$ singularity exec <container> /usr/local/bin/prepare_clusters.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_clusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_clusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_singletons.py

```bash
$ singularity exec <container> /usr/local/bin/remove_singletons.py
$ podman run --it --rm --entrypoint /usr/local/bin/remove_singletons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_singletons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reverse_bed.py

```bash
$ singularity exec <container> /usr/local/bin/reverse_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/reverse_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reverse_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-topology

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-topology
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-info

```bash
$ singularity exec <container> /usr/local/bin/hwloc-info
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ls

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ls
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-patch

```bash
$ singularity exec <container> /usr/local/bin/hwloc-patch
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ps

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ps
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lstopo

```bash
$ singularity exec <container> /usr/local/bin/lstopo
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lstopo-no-graphics

```bash
$ singularity exec <container> /usr/local/bin/lstopo-no-graphics
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
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
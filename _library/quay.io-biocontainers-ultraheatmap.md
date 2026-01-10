---
layout: container
name:  "quay.io/biocontainers/ultraheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultraheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ultraheatmap/container.yaml"
updated_at: "2026-01-10 04:00:38.314457"
latest: "1.3.1--py_1"
container_url: "https://biocontainers.pro/tools/ultraheatmap"
aliases:
 - "addFeatureToMatrix"
 - "alignmentSieve"
 - "bamCompare"
 - "bamCoverage"
 - "bamPEFragmentSize"
 - "bigwigCompare"
 - "computeGCBias"
 - "computeMatrix"
 - "computeMatrixOperations"
 - "computeOrderedMatrix"
 - "correctGCBias"
 - "deeptools"
 - "estimateReadFiltering"
 - "estimateScaleFactor"
 - "multiBamSummary"
 - "multiBigwigSummary"
 - "plotCorrelation"
 - "plotCoverage"
 - "plotEnrichment"
 - "plotFingerprint"
 - "plotHeatmap"
 - "plotPCA"
 - "plotProfile"
 - "ultraheatmap"
 - "gffutils-cli"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "activate-global-python-argcomplete"
versions:
 - "1.3.1--py_1"
description: "shpc-registry automated BioContainers addition for ultraheatmap"
config: {"url": "https://biocontainers.pro/tools/ultraheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultraheatmap", "latest": {"1.3.1--py_1": "sha256:cedbdbafd98c62e90b0fe5c865259ccbc9b4f4582318a71303613b675415f83e"}, "tags": {"1.3.1--py_1": "sha256:cedbdbafd98c62e90b0fe5c865259ccbc9b4f4582318a71303613b675415f83e"}, "docker": "quay.io/biocontainers/ultraheatmap", "aliases": {"addFeatureToMatrix": "/usr/local/bin/addFeatureToMatrix", "alignmentSieve": "/usr/local/bin/alignmentSieve", "bamCompare": "/usr/local/bin/bamCompare", "bamCoverage": "/usr/local/bin/bamCoverage", "bamPEFragmentSize": "/usr/local/bin/bamPEFragmentSize", "bigwigCompare": "/usr/local/bin/bigwigCompare", "computeGCBias": "/usr/local/bin/computeGCBias", "computeMatrix": "/usr/local/bin/computeMatrix", "computeMatrixOperations": "/usr/local/bin/computeMatrixOperations", "computeOrderedMatrix": "/usr/local/bin/computeOrderedMatrix", "correctGCBias": "/usr/local/bin/correctGCBias", "deeptools": "/usr/local/bin/deeptools", "estimateReadFiltering": "/usr/local/bin/estimateReadFiltering", "estimateScaleFactor": "/usr/local/bin/estimateScaleFactor", "multiBamSummary": "/usr/local/bin/multiBamSummary", "multiBigwigSummary": "/usr/local/bin/multiBigwigSummary", "plotCorrelation": "/usr/local/bin/plotCorrelation", "plotCoverage": "/usr/local/bin/plotCoverage", "plotEnrichment": "/usr/local/bin/plotEnrichment", "plotFingerprint": "/usr/local/bin/plotFingerprint", "plotHeatmap": "/usr/local/bin/plotHeatmap", "plotPCA": "/usr/local/bin/plotPCA", "plotProfile": "/usr/local/bin/plotProfile", "ultraheatmap": "/usr/local/bin/ultraheatmap", "gffutils-cli": "/usr/local/bin/gffutils-cli", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultraheatmap.
shpc-registry automated BioContainers addition for ultraheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultraheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultraheatmap:1.3.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultraheatmap/1.3.1--py_1
$ module help quay.io/biocontainers/ultraheatmap/1.3.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultraheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultraheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultraheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultraheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultraheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultraheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addFeatureToMatrix

```bash
$ singularity exec <container> /usr/local/bin/addFeatureToMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/addFeatureToMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addFeatureToMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignmentSieve

```bash
$ singularity exec <container> /usr/local/bin/alignmentSieve
$ podman run --it --rm --entrypoint /usr/local/bin/alignmentSieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignmentSieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamCompare

```bash
$ singularity exec <container> /usr/local/bin/bamCompare
$ podman run --it --rm --entrypoint /usr/local/bin/bamCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamCoverage

```bash
$ singularity exec <container> /usr/local/bin/bamCoverage
$ podman run --it --rm --entrypoint /usr/local/bin/bamCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamPEFragmentSize

```bash
$ singularity exec <container> /usr/local/bin/bamPEFragmentSize
$ podman run --it --rm --entrypoint /usr/local/bin/bamPEFragmentSize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamPEFragmentSize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigCompare

```bash
$ singularity exec <container> /usr/local/bin/bigwigCompare
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeGCBias

```bash
$ singularity exec <container> /usr/local/bin/computeGCBias
$ podman run --it --rm --entrypoint /usr/local/bin/computeGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeMatrix

```bash
$ singularity exec <container> /usr/local/bin/computeMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/computeMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeMatrixOperations

```bash
$ singularity exec <container> /usr/local/bin/computeMatrixOperations
$ podman run --it --rm --entrypoint /usr/local/bin/computeMatrixOperations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeMatrixOperations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeOrderedMatrix

```bash
$ singularity exec <container> /usr/local/bin/computeOrderedMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/computeOrderedMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeOrderedMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correctGCBias

```bash
$ singularity exec <container> /usr/local/bin/correctGCBias
$ podman run --it --rm --entrypoint /usr/local/bin/correctGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correctGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deeptools

```bash
$ singularity exec <container> /usr/local/bin/deeptools
$ podman run --it --rm --entrypoint /usr/local/bin/deeptools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeptools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimateReadFiltering

```bash
$ singularity exec <container> /usr/local/bin/estimateReadFiltering
$ podman run --it --rm --entrypoint /usr/local/bin/estimateReadFiltering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimateReadFiltering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimateScaleFactor

```bash
$ singularity exec <container> /usr/local/bin/estimateScaleFactor
$ podman run --it --rm --entrypoint /usr/local/bin/estimateScaleFactor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimateScaleFactor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiBamSummary

```bash
$ singularity exec <container> /usr/local/bin/multiBamSummary
$ podman run --it --rm --entrypoint /usr/local/bin/multiBamSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiBamSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiBigwigSummary

```bash
$ singularity exec <container> /usr/local/bin/multiBigwigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/multiBigwigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiBigwigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotCorrelation

```bash
$ singularity exec <container> /usr/local/bin/plotCorrelation
$ podman run --it --rm --entrypoint /usr/local/bin/plotCorrelation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotCorrelation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotCoverage

```bash
$ singularity exec <container> /usr/local/bin/plotCoverage
$ podman run --it --rm --entrypoint /usr/local/bin/plotCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotEnrichment

```bash
$ singularity exec <container> /usr/local/bin/plotEnrichment
$ podman run --it --rm --entrypoint /usr/local/bin/plotEnrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotEnrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotFingerprint

```bash
$ singularity exec <container> /usr/local/bin/plotFingerprint
$ podman run --it --rm --entrypoint /usr/local/bin/plotFingerprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotFingerprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHeatmap

```bash
$ singularity exec <container> /usr/local/bin/plotHeatmap
$ podman run --it --rm --entrypoint /usr/local/bin/plotHeatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHeatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotPCA

```bash
$ singularity exec <container> /usr/local/bin/plotPCA
$ podman run --it --rm --entrypoint /usr/local/bin/plotPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotProfile

```bash
$ singularity exec <container> /usr/local/bin/plotProfile
$ podman run --it --rm --entrypoint /usr/local/bin/plotProfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotProfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ultraheatmap

```bash
$ singularity exec <container> /usr/local/bin/ultraheatmap
$ podman run --it --rm --entrypoint /usr/local/bin/ultraheatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ultraheatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
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
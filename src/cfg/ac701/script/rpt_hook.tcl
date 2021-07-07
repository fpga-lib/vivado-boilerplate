puts "\nGenerate reports"

append runs_dir $PROJECT_NAME ".runs"
append util_rpt_name $TOP_NAME "_final_utilization.rpt"
append timing_rpt_name $TOP_NAME "_final_timing.rpt"
set util_rpt_path   [file join $BUILD_DIR "syn" $runs_dir "impl_1" $util_rpt_name]
set timing_rpt_path [file join $BUILD_DIR "syn" $runs_dir "impl_1" $timing_rpt_name]
report_utilization -file $util_rpt_path
report_timing_summary -file $timing_rpt_path

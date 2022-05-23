var advanced = <?php $out = array();
foreach (glob('*.pdf') as $filename) {
    $p = pathinfo($filename);
    $out[] = $p['filename'];
}
echo json_encode($out); ?>;
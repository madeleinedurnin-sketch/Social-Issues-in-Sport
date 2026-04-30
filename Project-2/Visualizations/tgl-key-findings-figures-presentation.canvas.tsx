import { BarChart, Divider, Grid, H1, H2, PieChart, Stack, Stat, Text } from "cursor/canvas";

export default function TGLKeyFindingsFiguresPresentation() {
  return (
    <Stack gap={24}>
      <H1>TGL Key Findings (Presentation Version)</H1>
      <Grid columns={4} gap={16}>
        <Stat value="355" label="Videos" />
        <Stat value="6,102" label="Comments" />
        <Stat value="695" label="Model-specific comments" />
        <Stat value="43.6%" label="Neutral/other" tone="info" />
      </Grid>

      <Divider />

      <H2>Figure 1: Creator Framing</H2>
      <BarChart
        categories={["Commercial", "Technology", "Combined"]}
        series={[
          { name: "Count", data: [313, 278, 243] },
          { name: "Percent", data: [88.2, 78.3, 68.5] },
        ]}
        height={360}
      />
      <Text tone="secondary" size="small">
        313/355 commercial framing (88.2%), 278/355 technology framing (78.3%),
        243/355 combined framing (68.5%).
      </Text>

      <Divider />

      <H2>Figure 2: Audience Sentiment Split</H2>
      <Grid columns={2} gap={18}>
        <PieChart
          donut
          size={360}
          data={[
            { label: "Resistance 24.9% (173)", value: 173, tone: "danger" },
            { label: "Acceptance 22.4% (156)", value: 156, tone: "success" },
            { label: "Ambivalence 9.1% (63)", value: 63, tone: "warning" },
            { label: "Neutral/Other 43.6% (303)", value: 303, tone: "neutral" },
          ]}
        />
        <BarChart
          categories={["Resistance", "Acceptance", "Ambivalence", "Neutral/Other"]}
          series={[{ name: "Percent", data: [24.9, 22.4, 9.1, 43.6] }]}
          height={360}
          valueSuffix="%"
        />
      </Grid>

      <Divider />

      <H2>Figure 3: Acceptance vs Resistance</H2>
      <Grid columns={3} gap={16}>
        <Stat value="24.9%" label="Resistance" tone="danger" />
        <Stat value="22.4%" label="Acceptance" tone="success" />
        <Stat value="2.5 pp" label="Gap" tone="warning" />
      </Grid>
    </Stack>
  );
}

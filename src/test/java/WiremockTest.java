import com.github.tomakehurst.wiremock.junit.WireMockRule;
import org.junit.Rule;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class WiremockTest {

    @Rule
    public WireMockRule wireMockRule = new WireMockRule(8000);

    @Test
    public void shouldStartWiremock() {
        assertEquals("test", 1, 1);
    }

}

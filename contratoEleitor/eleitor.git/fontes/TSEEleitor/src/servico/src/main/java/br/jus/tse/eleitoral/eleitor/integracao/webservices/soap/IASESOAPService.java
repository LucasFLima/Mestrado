package br.jus.tse.eleitoral.eleitor.integracao.webservices.soap;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.ASEDTO;

@WebService(
	targetNamespace = "http://tse.jus.br/eleitoral/eleitor"
)
@SOAPBinding(style = Style.RPC)
public interface IASESOAPService {
	
	@WebMethod
	public String inserirASE(ASEDTO aseDTO) throws WebServicesException;
	
}
